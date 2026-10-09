import sqlite3

conexao = sqlite3.connect("banco_ambiente.db")
cursor = conexao.cursor()

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")


comando_sql = "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)"

try:
   cursor.execute(comando_sql, (usuario, senha))
   conexao.commit()

   print(f"Usuário {usuario} inserido com sucesso!")
except sqlite3.IntegrityError:
   print("Erro: Usuário já cadastrado.")
except Exception as e: 
   print(f"Erro ao inserir usuário: {e}")

conexao.close()

