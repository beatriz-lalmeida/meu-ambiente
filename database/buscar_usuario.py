import sqlite3

conexao = sqlite3.connect("banco_ambiente.db")
cursor = conexao.cursor()

id_busca = input("Digite o ID do usuário: ")

comando_sql = "SELECT usuario, senha FROM usuarios WHERE id = ?"
cursor.execute(comando_sql, (id_busca,))

usuario = cursor.fetchone()

conexao.close()

if usuario:
  print(f"Usuário encontrado: {usuario[0]} ({usuario[1]})")
else:
  print("Usuário não encontrado")
