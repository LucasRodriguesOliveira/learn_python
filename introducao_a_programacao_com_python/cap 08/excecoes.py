nomes = ["Ana", "Carlos", "Maria"]

for tentativa in range(3):
  try:
    i = int(input("Digite um indice que quer imprimir:"))
    print(nomes[i])
  except ValueError:
    print("Digite um número!")
  except IndexError:
    print("Valor inválido, digite entre -3 e 3")
