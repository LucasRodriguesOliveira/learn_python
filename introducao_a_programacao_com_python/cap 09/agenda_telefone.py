# Programa 9.6 - Controle de uma agenda de telefones

agenda = []

def pede_nome():
  return input("Nome: ")

def pede_telefone():
  return input("Telefone: ")

def mostra_dados(nome, telefone):
  print(f"Nome: {nome} - Telefone: {telefone}")

def pede_nome_arquivo():
  return input("Nome do arquivo: ")

def pesquisa(nome):
  mnome = nome.lower()

  for p, e in enumerate(agenda):
    if e[0].lower() == mnome:
      return p

  return None

def novo():
  global agenda

  nome = pede_nome()
  telefone = pede_telefone()

  agenda.append([nome, telefone])

def apaga():
  global agenda
  nome = pede_nome()

  p = pesquisa(nome)

  if p is not None:
    del agenda[p]
  else:
    print("Nome não encontrado.")

def altera():
  p = pesquisa(pede_nome())

  if p is not None:
    nome, telefone = agenda[p]

    print("Encontrado:")
    mostra_dados(nome, telefone)

    nome = pede_nome()
    telefone = pede_telefone()
    agenda[p] = [nome, telefone]
  else:
    print("Nome não encontrado.")

def lista():
  global agenda
  print("\nAgenda\n")
  print("-" * 10)

  for e in agenda:
    mostra_dados(*e)
  print("-" * 10, end="\n\n")

def le():
  global agenda
  nome_arquivo = pede_nome_arquivo()
  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    agenda = []
    for l in arquivo.readlines():
      nome, telefone = l.strip().split("#")
      agenda.append([nome, telefone])

def grava():
  global agenda
  nome_arquivo = pede_nome_arquivo()
  with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    for nome, telefone in agenda:
      arquivo.write(f"{nome}#{telefone}\n")

def valida_faixa_inteiro(pergunta, inicio, fim):
  while True:
    try:
      valor = int(input(pergunta))
      if inicio <= valor <= fim:
        return valor
    except ValueError:
      print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
  print("""
1 - Novo
2 - Alterar
3 - Apagar
4 - Listar
5 - Gravar
6 - Ler

0 - Sair
""")
  return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)

while True:
  print(f"Agenda [{len(agenda)}]")
  opcao = menu()

  if opcao == 0:
    break
  elif opcao == 1:
    novo()
  elif opcao == 2:
    altera()
  elif opcao == 3:
    apaga()
  elif opcao == 4:
    lista()
  elif opcao == 5:
    grava()
  elif opcao == 6:
    le()
