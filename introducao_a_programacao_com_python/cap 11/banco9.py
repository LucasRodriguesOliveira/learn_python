import sqlite3
from contextlib import closing

with sqlite3.connect("brasil.db") as connection:
  connection.row_factory = sqlite3.Row
  print(f"{'Id':3s} {'Estado':-^20} {'Populacao':12s}")
  print("=" * 37)

  for estado in connection.execute("SELECT * FROM estados ORDER BY populacao"):
    print(f"{estado['id']:3d} {estado['nome']:-^20} {estado['populacao']:12d}")
