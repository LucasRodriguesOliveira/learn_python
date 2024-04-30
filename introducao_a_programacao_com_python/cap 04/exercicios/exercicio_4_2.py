# Escreva um programa que pergunte a velocidade de um carro de um usuário.
# Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Neste caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h

speed = float(input("Digite a velocidade do carro: "))
max_speed = 80
fine_per_km = 5

if speed > max_speed:
  print("Você foi multado!")
  fine = (speed - max_speed) * fine_per_km
  print(f"Valor da multa: R$ {fine:5.2f}")
