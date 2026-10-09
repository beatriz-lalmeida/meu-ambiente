import sqlite3

conexao = sqlite3.connect("banco_ambiente.db")
cursor = conexao.cursor()


id_para_deletar = input("Digite o ID do usuário que você quer excluir: ")

comando_delete = "DELETE FROM usuarios WHERE id = ?" 
cursor.execute(comando_delete, (id_para_deletar,))

conexao.commit()
conexao.close()

if cursor.rowcount > 0: 
  print(f"Usuário de id {id_para_deletar} deletado com sucesso!")
else:
  print("Nenhum usuário encontrado com este ID.")