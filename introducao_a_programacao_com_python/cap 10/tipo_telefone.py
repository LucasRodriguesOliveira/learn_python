from functools import total_ordering

@total_ordering
class TipoTelefone:
  def __init__(self, tipo: str):
    self.tipo = tipo

  def __str__(self) -> str:
    return f"({self.tipo})"

  def __eq__(self, outro) -> bool:
    if outro is None:
      return False

    return self.tipo == outro.tipo
  
  def __lt__(self, outro) -> bool:
    return self.tipo < outro.tipo

