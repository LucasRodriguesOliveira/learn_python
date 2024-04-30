# Programa 4.5 - Conta de telefone com três faixas de preço

minutos = int(input("Quantos minutos você utilizou este mês: "))

if minutos < 200:
  preco = 0.2
else:
  if minutos < 400:
    preco = 0.18
  else:
    preco = 0.15

print(f"Você vai pagar este mês: R$ {minutos * preco:6.2f}")
