import os

os.chdir("a")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("b")
print(os.getcwd())
os.chdir("../c")
print(os.getcwd())

os.mkdir("d")
os.mkdir("e")
os.mkdir("f")

print(os.getcwd())
os.chdir("d")
print(os.getcwd())
os.chdir("../e")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("f")
print(os.getcwd())

os.makedirs("avo/pai/filho")
os.makedirs("avo/mae/filha")

os.mkdir("velho")
os.rename("velho", "novo")

os.rename("avo/pai/filho", "avo/mae/filho")

open("teste.txt", "w").close()

os.mkdir("vago")
os.rmdir("vago")
os.remove("teste.txt")

os.chdir("..")

print(os.listdir("."))
print(os.listdir("f"))
print(os.listdir("d"))
print(os.listdir("f/avo"))
print(os.listdir("f/avo/pai"))
print(os.listdir("f/avo/mae"))
