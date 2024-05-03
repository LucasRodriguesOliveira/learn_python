import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as con:
  with closing(con.cursor()) as cursor:
    cursor.execute("select * from agenda where nome = 'Lucas'")

    while True:
      result = cursor.fetchone()
      if result is None:
        break

      print(f"Nome: {result[0]}")
      print(f"Telefone: {result[1]}")
