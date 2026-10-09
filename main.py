import sqlite3

conexao = sqlite3.connect("banco_ambiente.db")
cursor = conexao.cursor()

comando_sql = """
CREATE TABLE IF NOT EXISTS usuarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  usuario TEXT NOT NULL,
  senha TEXT NOT NULL
)
"""
cursor.execute(comando_sql)

conexao.commit()
 
conexao.close()

print("Banco de dados")
