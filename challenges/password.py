import random
from tkinter import Tk

letters = [chr(x) for x in list(range(65, 91))]
symbols = ['@', '#', '$', '%', '&', '*', '+', '-', '/', '!']
numbers = list(range(10))

print("Gerador de senhas")
size = int(input("Informe o tamanho da senha: "))
password = []

for tries in range(3):
    print("Escolha uma das opções de senha")
    print("[L]: Letras minúsculas")
    print("[U]: Letras maiúsculas")
    print("[S]: Símbolos")
    print("[N]: Números")
    print("""
Pode adicionar mais de uma opção (LSN -> letras minusculas, simbolos e números)
""")

    choices = input("Opção: ")

    if len(choices) == 0 or not choices.strip():
        print("Pelo menos uma opção deve ser escolhida!")
        continue

    invalid = False
    for letter in choices:
        if letter.lower() not in "lusn":
            print("Opcao inválida")
            invalid = True
            break
    else:
        invalid = False

    if invalid:
        continue
    else:
        break
else:
    print("Máximo de tentativas")
    exit(1)

while len(password) < size:
    if len(choices) == 1:
        option = choices
    else:
        option, = random.sample(list(choices), 1)

    option = option.lower()

    if option == 'l':
        item, = random.sample(letters, 1)
        item = item.lower()
    elif option == 'u':
        item, = random.sample(letters, 1)
    elif option == 'n':
        item, = random.sample(numbers, 1)
        item = str(item)
    else:
        item, = random.sample(symbols, 1)

    password.append(item)

password = "".join(password)

print()
print(password)
print()
print("Salvar na área de transferência?")
print("[S] -> sim")
print("[N] -> não")
should_save = input("opção: ")

if should_save.strip().lower() == 's':
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(password)
    r.update()
    r.destroy()
    print("Salvo na área de transferência")
