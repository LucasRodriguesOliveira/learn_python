nome = "Lucas"
idade = 26
dinheiro = 507.85

print("{} tem {} anos e R${} no bolso.".format(nome, idade, dinheiro))
print("{:12} tem {:3} anos e R${:5.2f} no bolso.".format(nome, idade, dinheiro))
print("{:12} tem {:03}anos e R${:5.2f} no bolso.".format(nome, idade, dinheiro))
print("{:<12s} tem {:<3} anos e R${:5.2f} no bolso.".format(nome, idade, dinheiro))
