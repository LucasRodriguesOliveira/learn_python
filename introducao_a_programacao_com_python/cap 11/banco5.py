import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as connection:
  with closing(connection.cursor()) as cursor:
    cursor.execute("""
      DELETE FROM agenda WHERE  nome = 'Maria'
    """)

    print("Registros apagados: ", cursor.rowcount)

    if cursor.rowcount == 1:
      connection.commit()
    else:
      connection.rollback()
      print("Alterações abortadas")
