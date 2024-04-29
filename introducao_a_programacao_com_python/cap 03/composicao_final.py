nome = "Lucas"
idade = 26
dinheiro = 507.85

print("%s tem %d anos e R$%f no bolso." % (nome, idade, dinheiro))
print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, dinheiro))
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, dinheiro))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, dinheiro))
