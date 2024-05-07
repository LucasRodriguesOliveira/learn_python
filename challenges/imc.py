print("Calculo IMC")

ranges = {
  "abaixo": ["Abaixo do peso", 18.5],
  "normal": ["Peso Normal", 25],
  "sobrepeso": ["Sobrepeso", 30],
  "obeso": ["Obeso", None]
}

weight = float(input("Informe seu peso em Kg: "))
height = float(input("Informe sua altura em Metros: "))

imc = weight / (height ** 2)

for title, value in ranges.values():
  if value is not None and imc < value:
    print(f"IMC: {title}")
    break
else:
  print(f"IMC: {ranges['obeso']}")
