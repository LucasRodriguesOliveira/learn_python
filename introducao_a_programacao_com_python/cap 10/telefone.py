from tipo_telefone import TipoTelefone

class Telefone:
  def __init__(self, numero: str, tipo: TipoTelefone = None):
    self.numero = numero
    self.tipo = tipo

  def __str__(self) -> str:
    if self.tipo is not None:
      tipo = self.tipo
    else:
      tipo = ""

    return f"{self.numero} {tipo}"

  def __eq__(self, outro) -> bool:
    return self.numero == outro.numero and (
      (self.tipo == outro.tipo) or
      (self.tipo is None or outro.tipo is None)
    )

  @property
  def numero(self):
    return self.__numero

  @numero.setter
  def numero(self, valor: str):
    if valor is None or not valor.strip():
      raise ValueError("Número não pode ser None ou em branco")

    self.__numero = valor
