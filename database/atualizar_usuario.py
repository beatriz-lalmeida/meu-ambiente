import sqlite3

conexao = sqlite3.connect("banco_ambiente.db")
cursor = conexao.cursor()

id_usuario = input("Digite o ID do usuário que você quer atualizar: ")
nova_senha = input("Digite a nova senha: ")


comando_update = "UPDATE usuarios SET senha = ? WHERE id = ?"
cursor.execute(comando_update, (nova_senha, id_usuario))

conexao.commit
conexao.close()

if cursor.rowcount > 0: 
  print(f"Usuário de id {id_usuario} atualizado com sucesso!")
else:
  print("Nenhum usuário encontrado com este ID.")