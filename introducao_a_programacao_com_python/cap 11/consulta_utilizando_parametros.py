# Programa 11.5 - Consulta utilizando parâmetros

import sqlite3
from contextlib import closing

nome = input("Nome a selecionar: ")

with sqlite3.connect("agenda.db") as connection:
  with closing(connection.cursor()) as cursor:
    cursor.execute('SELECT * FROM agenda WHERE nome = ?', (nome,))
    x = 0

    while True:
      result = cursor.fetchone()
      if result is None:
        if x == 0:
          print("Nada encontrado.")
        break
      print(f"Nome: {result[0]}")
      print(f"Telefone: {result[1]}")
      x += 1
