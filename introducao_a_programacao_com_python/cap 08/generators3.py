def gerador_de_numeros():
  i = 0

  while True:
    yield i
    i += 1

g = gerador_de_numeros()
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
