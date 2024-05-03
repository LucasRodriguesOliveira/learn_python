import sqlite3

with sqlite3.connect("agenda.db") as connection:
  for result in connection.execute("SELECT * FROM agenda"):
    print(f"Nome: {result[0]}")
    print(f"Telefone: {result[1]}")
