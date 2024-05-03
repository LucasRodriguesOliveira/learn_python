import valida

class Menu:
  def __init__(self) -> None:
    self.opcoes = [["Sair", None]]

  def adiciona_opcao(self, nome: str, funcao):
    self.opcoes.append([nome, funcao])

  def exibe(self):
    print("=" * 10)
    print("Menu")
    print("=" * 10, end="\n\n")

    for indice, opcao in enumerate(self.opcoes):
      nome_opcao = opcao[0]
      print(f"[{indice}] - {nome_opcao}")
    print()

  def execute(self):
    while True:
      self.exibe()
      escolha = valida.faixa_inteiro(
        "Escolha uma opção: ",
        0,
        len(self.opcoes) - 1
      )

      if escolha == 0:
        break
      self.opcoes[escolha][1]()

