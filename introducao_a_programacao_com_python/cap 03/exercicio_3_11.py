# faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

price = float(input("Preço do produto: "))
porcentage = float(input("Informe a porcentagem de desconto: "))

discount = (price * porcentage) / 100
newprice = price - discount

print(f"O valor do desconto: {discount:5.2f}")
print(f"Valor a pagar: {newprice:5.2f}")

