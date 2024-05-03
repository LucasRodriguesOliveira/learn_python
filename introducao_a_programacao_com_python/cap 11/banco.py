import sqlite3

connection = sqlite3.connect("agenda.db")

cursor = connection.cursor()

cursor.execute('''
  CREATE TABLE agenda(
    nome     text,
    telefone text
  )
''')

cursor.execute("""
  INSERT INTO agenda(nome, telefone) values (?, ?)
""", ("Lucas", "9999-9999"))

connection.commit()
cursor.close()
connection.close()
