from cliente import Cliente
from conta import Conta

class Banco:
  def __init__(self, nome: str):
    self.nome = nome
    self.clientes: list[Cliente] = []
    self.contas: list[Conta] = []

  def abre_conta(self, conta: Conta):
    self.contas.append(conta)

  def lista_contas(self):
    for conta in self.contas:
      conta.resumo()
