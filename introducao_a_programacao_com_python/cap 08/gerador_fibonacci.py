def gerador_fibonnaci(max):
  p = 0
  s = 1

  while s < max:
    yield s
    p, s = s, s + p

print([x for x in gerador_fibonnaci(10)])
