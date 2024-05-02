# Programa 8.16 - Função lambda que recebe  um valor e retorna o dobro dele

a = lambda x: x * 2

print(a(3))

aumento = lambda a, b: (a * b / 100)

print(aumento(100, 5))

L = ["A", "b", "C", "d", "E"]
L.sort()

print(L)

L.sort(key=lambda k: k.lower())
print(L)
