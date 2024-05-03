# Programa 11.2 - Consulta registro por registro

import sqlite3

connection = sqlite3.connect("agenda.db")
cursor = connection.cursor()

cursor.execute("Select * from agenda")
while True:
  result = cursor.fetchone()
  if result is None:
    break

  print(f"Nome: {result[0]}")
  print(f"Telefone: {result[1]}")

cursor.close()
connection.close()
