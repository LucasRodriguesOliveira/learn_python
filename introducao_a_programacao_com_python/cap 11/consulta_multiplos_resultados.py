# Programa 11.1 - Consulta com múltiplos resultados

import sqlite3

connection = sqlite3.connect("agenda.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM agenda")

result = cursor.fetchall()

for data in result:
  print(f"Nome: {data[0]}")
  print(f"Telefone: {data[1]}")

cursor.close()
connection.close()
