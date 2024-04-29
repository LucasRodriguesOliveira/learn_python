# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos

dias = int(input("Informe os dias: "))
horas = int(input("Informe as horas: "))
minutos = int(input("Informe os minutos: "))
segundos = int(input("Informe os segundos: "))

total = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print(f"Total em segundos: {total}")
