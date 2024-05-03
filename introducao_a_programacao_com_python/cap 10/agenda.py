from lista_unica import Array
from dado_agenda import DadoAgenda
from lista_tipo_telefone import ListaTipoTelefone
from tipo_telefone import TipoTelefone
from nome import Nome

class Agenda(Array):
  def __init__(self):
    super().__init__(DadoAgenda)
    self.listaTipos = ListaTipoTelefone()

  def adicionaTipo(self, tipo: str):
    self.listaTipos.add(TipoTelefone(tipo))

  def pesquisaNome(self, nome: str | Nome) -> DadoAgenda | None:
    if isinstance(nome, str):
      nome = Nome(nome)

    for dados in self.array:
      if dados.nome == nome:
        return dados
    else:
      return None

  def ordena(self):
    super().sort(lambda dado: str(dado.nome))

