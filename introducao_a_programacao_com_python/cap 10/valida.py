def nulo_ou_vazio(texto: str) -> bool:
  return texto is None or not texto.strip()

def faixa_inteiro(pergunta: str, inicio: int, fim: int, padrao: str = None) -> int:
  while True:
    try:
      entrada = input(pergunta)
      if nulo_ou_vazio(entrada) and padrao is not None:
        entrada = padrao
      valor = int(entrada)

      if inicio <= valor <= fim:
        return valor
    except ValueError:
      print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def faixa_inteiro_ou_branco(pergunta: str, inicio: int, fim: int) -> int | None:
  while True:
    try:
      entrada = input(pergunta)

      if nulo_ou_vazio(entrada):
        return None

      valor = int(entrada)

      if inicio <= valor <= fim:
        return valor
    except ValueError:
      print(f"Valor inválido, favor digitar entre {inicio} e {fim}")
