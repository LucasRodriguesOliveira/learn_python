from cliente import Cliente

class Conta:
  def __init__(self, clientes: list[Cliente], numero: int, saldo: int = 0):
    self.saldo = 0
    self.clientes = clientes
    self.numero = numero
    self.operacoes = []
    self.deposito(saldo)

  def resumo(self):
    print(f"CC Nº: {self.numero}")
    print(f"\tSaldo: {self.saldo:10.2f}")

  def saque(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      self.operacoes.append(["SAQUE", valor])

  def deposito(self, valor):
    self.saldo += valor
    self.operacoes.append(["DEPÓSITO", valor])

  def extrato(self):
    print(f"Extrato CC Nº {self.numero}", end="\n\n")

    for op_nome, op_valor in self.operacoes:
      print(f"[{op_nome:^10s}]: R$ {op_valor:<10.2f}")

    print(f"\n\tSaldo: {self.saldo:10.2f}\n")
