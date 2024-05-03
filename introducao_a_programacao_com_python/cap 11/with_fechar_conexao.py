# Programa 11.3 - Uso do With para fechar a conexão

import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conn:
  with closing(conn.cursor()) as cursor:
    cursor.execute("select * from agenda")
    while True:
      result = cursor.fetchone()

      if result is None:
        break
      print(f"Nome: {result[0]}")
      print(f"Telefone: {result[1]}")
