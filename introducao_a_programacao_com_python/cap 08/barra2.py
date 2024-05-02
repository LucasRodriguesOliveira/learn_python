def barra(n=10, c="*"):
  print(c * n)

L = [[5, "-"], [10, "*"], [5], [6, "."]]

for e in L:
  barra(*e)
