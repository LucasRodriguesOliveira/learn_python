with open("multiplos de 4.txt", "w") as arquivo_multiplos4, open("pares.txt") as arquivo_pares:
  for l in arquivo_pares.readlines():
    if int(l) % 4 == 0:
      arquivo_multiplos4.write(l)
