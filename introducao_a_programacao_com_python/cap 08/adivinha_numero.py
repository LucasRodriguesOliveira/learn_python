# Programa 8.20 - Adivinhando o número
import random

n = random.randint(1, 10)

x = int(input("Escolha um número entre 1 e 10: "))

if x == n:
  print("Você acertou!")
else:
  print("Você errou")

print(f"Número: {n}")
