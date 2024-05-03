import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as connection:
  with closing(connection.cursor()) as cursor:
    cursor.execute("""
      UPDATE agenda
         SET telefone = '12345-6789'
       WHERE nome = 'Nilo'
    """)

    connection.commit()
