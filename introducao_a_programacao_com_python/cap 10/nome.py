from functools import total_ordering

@total_ordering
class Nome:
  def __init__(self, nome: str):
    self.nome = nome

  def __str__(self) -> str:
    return self.nome

  def __repr__(self) -> str:
    return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.nome} Chave: {self.chave} >"

  def __eq__(self, outro) -> bool:
    print("__eq__ chamado")
    return self.nome == outro.nome
  
  def __lt__(self, outro) -> bool:
    print("__lt__ chamado")
    return self.nome < outro.nome

  @property
  def nome(self) -> str:
    return self.__nome

  @nome.setter
  def nome(self, valor: str):
    if valor is None or not valor.strip():
      raise ValueError("Nome não pode ser nulo nem em branco")
    self.__nome = valor
    self.__chave = Nome.CriaChave(valor)

  @staticmethod
  def CriaChave(nome: str):
    return nome.strip().lower()
