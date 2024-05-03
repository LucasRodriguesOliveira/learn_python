import sqlite3

connection = sqlite3.connect("agenda.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM agenda")

result = cursor.fetchone()

print(f"Nome: {result[0]}")
print(f"Telefone: {result[1]}")

cursor.close()
connection.close()
