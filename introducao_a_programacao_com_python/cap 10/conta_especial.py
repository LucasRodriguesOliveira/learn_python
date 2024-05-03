from conta import Conta
from cliente import Cliente

class ContaEspecial(Conta):
  def __init__(self, clientes: list[Cliente], numero: int, saldo: int = 0, limite: int = 0):
    Conta.__init__(self, clientes, numero, saldo)
    self.limite = limite

  def saque(self, valor):
    if self.saldo + self.limite >= valor:
      self.saldo -= valor
      self.operacoes.append(["SAQUE", valor])
