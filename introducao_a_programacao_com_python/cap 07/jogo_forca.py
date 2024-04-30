# Programa 7.2 - Jogo da Forca

word = input("Digite a palavra secreta:").lower().strip()

for x in range(100):
  print()

tries = []
hits = []
fails = 0

while True:
  password = ""

  for letter in word:
    password += letter if letter in hits else "."

  print(password)

  if password == word:
    print("Você acertou!")
    break

  user_try = input("\nDigite uma letra:").lower().strip()

  if user_try in tries:
    print("Você já tentou esta letra")
    continue
  else:
    tries += user_try
    if user_try in word:
      hits += user_try
    else:
      fails += 1
      print("Você errou!")

  print("X==:==\nX  :  ")
  print("X  0  " if fails >= 1 else "X")

  row2 = ""

  if fails == 2:
    row2 = "  |  "
  elif fails == 3:
    row2 = " \|  "
  elif fails >= 4:
    row2 = " \|/ "
  print(f"X{row2}")

  row3 = ""

  if fails == 5:
    row3 += " /   "
  elif fails >= 6:
    row3 += " / \ "
  print(f"X{row3}")

  print("X\n=============")

  if fails == 6:
    print("Enforcado!")
    break
