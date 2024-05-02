# Programa 9.5 - Processamento de um arquivo

WIDTH = 79

with open("entrada.txt") as file:
  for row in file.readlines():
    if row[0] == ";":
      continue
    elif row[0] == ">":
      print(row[1:].rjust(WIDTH))
    elif row[0] == "*":
      print(row[1:].center(WIDTH))
    else:
      print(row)
