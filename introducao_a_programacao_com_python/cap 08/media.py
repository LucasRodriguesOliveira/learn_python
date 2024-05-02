def soma(L):
  total = 0

  for i in L:
    total += i

  return total

def media(L):
  return soma(L) / len(L)

L = [10, 20, 25, 30]
M = [15, 16, 17, 18, 35]

print(media(L))
print(media(M))
