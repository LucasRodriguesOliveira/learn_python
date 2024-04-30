# Programa 6.21 - Obtenção do preço com um dicionário

tabela = {
  "Alface": 0.45,
  "Batata": 1.2,
  "Tomate": 2.3,
  "Feijão": 1.5
}

while True:
  print(tabela)
  produto = input("Digite o nome do produto, fim para terminar: ")

  if produto == "fim":
    break

  if produto in tabela:
    print(f"Preço: {tabela[produto]:5.2f}")
  else:
    print("Produto não encontrado!")
