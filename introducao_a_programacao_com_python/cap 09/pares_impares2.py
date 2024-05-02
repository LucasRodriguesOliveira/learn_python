# Programa 9.3 - Gravação de números pares e ímpares em arquivos diferentes

with open("impares.txt", "w") as arquivo_impares, open("pares.txt", "w") as arquivo_pares:
  for n in range(0, 1000):
    if n % 2 == 0:
      arquivo_pares.write(f"{n}\n")
    else:
      arquivo_impares.write(f"{n}\n")
