from dado_agenda import DadoAgenda
from agenda import Agenda
from menu import Menu
from tipo_telefone import TipoTelefone
from nome import Nome
from telefone import Telefone
import valida
import pickle

class AppAgenda:
  @staticmethod
  def pede_nome():
    return input("Nome: ")

  @staticmethod
  def pede_telefone():
    return input("Telefone: ")

  @staticmethod
  def mostra_dados(dados: DadoAgenda):
    print(f"Nome: {dados.nome}")

    for telefone in dados.telefoneArray:
      print(f"Telefone: {telefone}")
    print()

  @staticmethod
  def mostra_dados_telefone(dados: DadoAgenda) -> None:
    print(f"Nome: {dados.nome}")

    for indice, telefone in enumerate(dados.telefoneArray):
      print(f"[{indice}] - Telefone: {telefone}")
    print()

  @staticmethod
  def pede_nome_arquivo() -> str:
    return input("Nome do arquivo: ")

  def __init__(self) -> None:
    self.agenda = Agenda()
    self.agenda.adicionaTipo("Celular")
    self.agenda.adicionaTipo("Residência")
    self.agenda.adicionaTipo("Trabalho")
    self.agenda.adicionaTipo("Fax")

    self.menu = Menu()
    self.menu.adiciona_opcao("Novo", self.novo)
    self.menu.adiciona_opcao("Alterar", self.altera)
    self.menu.adiciona_opcao("Apagar", self.apaga)
    self.menu.adiciona_opcao("Listar", self.lista)
    self.menu.adiciona_opcao("Gravar", self.grava)
    self.menu.adiciona_opcao("Ler", self.le)
    self.menu.adiciona_opcao("Ordernar", self.ordena)
    self.ultimo_nome = None

  def pede_tipo_telefone(self, padrao: str = None) -> TipoTelefone:
    for indice, tipo in enumerate(self.agenda.listaTipos):
      print(f" [{indice}] - {tipo}", end=None)

    t = valida.faixa_inteiro("Tipo: ", 0, len(self.agenda.listaTipos) - 1, padrao)
    return self.agenda.listaTipos[t]

  def pesquisa(self, nome: Nome) -> DadoAgenda | None:
    dado = self.agenda.pesquisaNome(nome)

    return dado

  def novo(self):
    novo = AppAgenda.pede_nome()

    if valida.nulo_ou_vazio(novo):
      return

    nome = Nome(novo)

    if self.pesquisa(nome) is not None:
      print("Nome já existe!")
      return

    registro = DadoAgenda(nome)
    self.menu_telefones(registro)
    self.agenda.add(registro)

  def menu_telefones(self, dados: DadoAgenda) -> None:
    while True:
      print("\nEditando telefones\n")
      AppAgenda.mostra_dados_telefone(dados)

      if len(dados.telefoneArray) > 0:
        print()
        print("[A] - alterar")
        print("[D] - apagar")
      print("[N] - novo")
      print("[S] - sair")
      print()

      operacao = input("Escolha uma operação: ")
      operacao = operacao.lower()

      if operacao not in ["a", "d", "n", "s"]:
        print("Operação inválida. Digite A, D, N, ou S")
        continue

      if operacao == 'a' and len(dados.telefoneArray) > 0:
        self.altera_telefones(dados)
      elif operacao == 'd' and len(dados.telefoneArray) > 0:
        self.apaga_telefone(dados)
      elif operacao == 'n':
        self.novo_telefone(dados)
      elif operacao == 's':
        break

  def altera_telefones(self, dados: DadoAgenda) -> None:
    t = valida.faixa_inteiro_ou_branco(
      "Digite a posição do número a alterar, enter para sair: ",
      0,
      len(dados.telefoneArray) - 1
    )

    if t is None:
      return

    telefone: Telefone = dados.telefoneArray[t]
    print(f"Telefone: {telefone}")
    print("Digite enter caso não queira alterar o número")

    novotelefone = AppAgenda.pede_telefone()

    if not valida.nulo_ou_vazio(novotelefone):
      telefone.numero = novotelefone

    print("Digite enter caso não queira alterar o tipo")
    telefone.tipo = self.pede_tipo_telefone(
      self.agenda.listaTipos.search(telefone.tipo)
    )

  def apaga_telefone(self, dados: DadoAgenda) -> None:
    t = valida.faixa_inteiro_ou_branco(
      "Digite a posição do número a apagar, enter para sair: ",
      0,
      len(dados.telefoneArray) - 1
    )

    if t is None:
      return

    dados.telefoneArray.remove(dados.telefoneArray[t])

  def novo_telefone(self, dados: DadoAgenda) -> None:
    telefone = AppAgenda.pede_telefone()

    if valida.nulo_ou_vazio(telefone):
      return

    if dados.pesquisaTelefone(telefone) is not None:
      print("Telefone já existe")

    tipo = self.pede_tipo_telefone()
    dados.telefoneArray.add(Telefone(telefone, tipo))

  def apaga(self) -> None:
    if len(self.agenda) == 0:
      print("Agenda vazia, nada a apagar")
      return

    nome = AppAgenda.pede_nome()

    if valida.nulo_ou_vazio(nome):
      return

    p = self.pesquisa(nome)

    if p is not None:
      self.agenda.remove(p)
      print(f"Apagado. A agenda agora possui apenas: {len(self.agenda)} registros")
    else:
      print("Nome não encontrado.")

  def altera(self) -> None:
    if len(self.agenda) == 0:
      print("Agenda vazia, nada a alterar")
      return

    nome = AppAgenda.pede_nome()

    if valida.nulo_ou_vazio(nome):
      return

    p = self.pesquisa(nome)

    if p is not None:
      print("\nEncontrado:", end="\n\n")
      AppAgenda.mostra_dados(p)
      print("Digite enter caso não queira alterar o nome")

      novo = AppAgenda.pede_nome()

      if not valida.nulo_ou_vazio(nome):
        p.nome = Nome(novo)

      self.menu_telefones(p)
    else:
      print("Nome não encontrado!")

  def lista(self) -> None:
    print("\nAgenda")
    print("-" * 60)

    for a in self.agenda:
      AppAgenda.mostra_dados(a)
    print("-" * 60)

  def le(self, nome_arquivo=None) -> None:
    if nome_arquivo is None:
      nome_arquivo = AppAgenda.pede_nome_arquivo()
    if valida.nulo_ou_vazio(nome_arquivo):
      return

    with open(nome_arquivo, "rb") as arquivo:
      self.agenda = pickle.load(arquivo)

    self.ultimo_nome = nome_arquivo

  def ordena(self) -> None:
    self.agenda.sort()
    print("\nAgenda ordenada", end="\n\n")

  def grava(self) -> None:
    if self.ultimo_nome is not None:
      print(f"Último nome utilizado foi '{self.ultimo_nome}'")
      print("Digite enter caso queira utilizar o mesmo nome")

    nome_arquivo = AppAgenda.pede_nome_arquivo()
    if valida.nulo_ou_vazio(nome_arquivo):
      if self.ultimo_nome is not None:
        nome_arquivo = self.ultimo_nome
      else:
        return

    with open(nome_arquivo, "wb") as arquivo:
      pickle.dump(self.agenda, arquivo)

  def execute(self) -> None:
    self.menu.execute()

