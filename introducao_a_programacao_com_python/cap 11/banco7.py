import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as connection:
  connection.row_factory = sqlite3.Row

  with closing(connection.cursor()) as cursor:
    for result in cursor.execute("SELECT * FROM agenda"):
      print(f"Nome: {result['nome']}")
      print(f"Telefone: {result['telefone']}")
  