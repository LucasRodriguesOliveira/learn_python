L = [x for x in range(10)]
print(L)

Z = [x * 2 for x in [0, 1, 2, 3]]
print(Z)

Y = [(x, x * 2) for x in [1, 2, 3]]
print(Y)

P = [x for x in range(10) if x % 2 == 0]
print(P)

D = [(y, x) for x, y in [(4, 3), (1, 2), (8, 9)]]
print(D)

G = [(x, y) for *x, y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
print(G)

import math

I = [math.sqrt(z) for z in range(0, 10)]
print(I)

H = [z for z in range(0, 10) if math.sqrt(z) % 1 == 0]
print(H)
