# Programa 6.24 - Exemplo de dicionario sem valor padrao

d = {}

for letra in "abracadabra":
  d[letra] = d.get(letra, 0) + 1

print(d)
