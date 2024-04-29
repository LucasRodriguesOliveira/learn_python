# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salario e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

salary = float(input("Informe o salário: "))
porcentage = float(input("Informe a porcentagem de aumento: "))

bonus = (salary * porcentage) / 100
newSalary = salary + bonus

print(f"O valor do aumento: {bonus:5.2f}")
print(f"O novo salário: {newSalary:5.2f}")
