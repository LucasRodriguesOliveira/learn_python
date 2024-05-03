from cliente import Cliente
from conta import Conta
from banco import Banco
from lista_unica import Array
from nome import Nome

joao = Cliente("João da Silva", "1234-4567")
maria = Cliente("Maria da Silva", "5555-4444")
jose = Cliente("José Vargas", "9999-9999")

conta_joao_maria = Conta([joao, maria], 100)
conta_jose = Conta([jose], 10)

banco = Banco("Tatú")
banco.abre_conta(conta_joao_maria)
banco.abre_conta(conta_jose)

banco.lista_contas()

unique_list = Array(int)
unique_list.add(5)
unique_list.add(6)

print(len(unique_list))

for el in unique_list:
  print(el)

unique_list.add(5)

print(len(unique_list))

print(unique_list[0])
print(unique_list[1])

A = Nome("Lucas")
print(A)

# B = Nome(" ")
# C = Nome(None)
print(A == Nome("Lucas"))
print(A != Nome("Lucas"))
print(A < Nome("Lucas"))
print(A > Nome("Lucas"))
