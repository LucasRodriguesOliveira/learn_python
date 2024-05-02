# Programa 8.15 - Função imprime_maior com número indeterminado de parâmetros

def imprime_maior(mensagem, *numeros):
  maior = None

  for e in numeros:
    if maior is None or maior < e:
      maior = e

  print(mensagem, maior)

imprime_maior("Maior: ", 5, 4, 3, 1)
imprime_maior("Max: ", *[1, 7, 9])
