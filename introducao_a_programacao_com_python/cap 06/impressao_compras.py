# Programa 6.18 - Impressao das compras

p1 = ["maçã", 10, 0.3]
p2 = ["pera", 5, 0.75]
p3 = ["kiwi", 4, 0.98]
compras = [p1, p2, p3]

for e in compras:
  print(f"Produto: {e[0]}")
  print(f"Quantidade: {e[1]}")
  print(f"Preço: {e[2]}")
