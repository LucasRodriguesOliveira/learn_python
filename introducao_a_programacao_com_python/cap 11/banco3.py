import sqlite3

dados = [
  ("João", "98901-0109"),
  ("André", "98902-8900"),
  ("Maria", "97897-3321")
]

connection = sqlite3.connect("agenda.db")
cursor = connection.cursor()

cursor.executemany("""
  INSERT INTO agenda(nome, telefone) VALUES (?, ?)
""", dados)

connection.commit()

cursor.close()
connection.close()
