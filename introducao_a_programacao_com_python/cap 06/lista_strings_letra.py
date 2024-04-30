# Programa 6.15 - Impressão de uma lista de strings, letra a letra

S = ["maçãs", "peras", "kiwis"]

for s in S:
  for l in s:
    print(l, end=", ")
  print()
