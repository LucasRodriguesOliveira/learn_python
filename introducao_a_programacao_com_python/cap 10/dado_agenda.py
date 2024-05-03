from lista_telefone import ListaTelefone
from telefone import Telefone
from nome import Nome

class DadoAgenda:
  def __init__(self, nome: Nome):
    self.nome = nome
    self.telefoneArray = ListaTelefone()

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, valor: Nome):
    if not isinstance(valor, Nome):
      raise TypeError("nome deve ser uma instância da classe Nome")

    self.__nome = valor

  def pesquisaTelefone(self, telefone: str):
    posicao = self.telefoneArray.search(Telefone(telefone))

    if posicao == -1:
      return None
    else:
      return self.telefoneArray[posicao]
