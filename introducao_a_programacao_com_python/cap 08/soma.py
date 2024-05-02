# Programa 8.19 - Módulo soma (soma.py) que importa entrada

# import entrada
from entrada import valida_inteiro

L = []
for x in range(10):
  L.append(valida_inteiro("Digite um número: ", 0, 20))

print(f"Soma: {sum(L)}")
