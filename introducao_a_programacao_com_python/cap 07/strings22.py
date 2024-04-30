print("{0} {1}".format("Hello", "World"))
print("{0} x {1} R${2}".format(5, "maçã", "1.20"))

print("{0} {1} {0}".format("-", "x"))
print("{1} {0}".format("primeiro", "segundo"))

print("{0:10} {1}".format("123", "456"))
print("X{0:10}X".format("123"))
print("X{0:10}X".format("123456789012345"))

print("X{0:<10}X".format("123"))
print("X{0:>10}X".format("123"))
print("X{0:^10}X".format("123"))

print("X{0:.<10}X".format("123"))
print("X{0:!>10}X".format("123"))
print("X{0:*^10}X".format("123"))

print("{0[0]} {0[1]}".format(["123", "456"]))
print("{0[nome]} {0[telefone]}".format({"telefone": 572, "nome": "Maria"}))
