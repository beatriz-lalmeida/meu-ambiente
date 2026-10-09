import sqlite3

conexao = sqlite3.connect("banco_ambiente.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

print("Lista de usuários cadastrados:")
for usuario in usuarios:
    print(f"ID: {usuario[0]}, Usuário: {usuario[1]}, Senha: {usuario[2]}")


conexao.close() 