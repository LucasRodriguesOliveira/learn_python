def prime(n=10):
  for x in range(2, n):
    for y in range(x // 2):
      if x % (y + 1) == 0 and (y + 1) != 1:
        break
    else:
      yield x



print([x for x in prime(22)])
