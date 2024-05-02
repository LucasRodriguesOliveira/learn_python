def soma(*n):
  total = 0

  for x in n:
    total += x

  return total

print(soma(1, 2))
print(soma(2))
print(soma(5, 6, 7, 8))
print(soma(9, 10, 11, 20, 30, 40))
