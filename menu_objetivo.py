print("1 - Foco")
print("2 - Descanso")
print("3 - Visita")
print("4 - Relaxamento")
print("5 - Cinema")

opcao = input(str("Qual o seu objetivo? "))

if opcao == "1":
  print("Vamos preparar o ambiente para Foco!")
elif opcao == "2":
  print("Vamos preparar o ambiente para Descanso!")
elif opcao == "3":
  print("Vamos preparar o ambiente para Visita!")
elif opcao == "4":
  print("Vamos preparar o ambiente para Relaxamento!")
elif opcao == "5":
  print("Vamos preparar o ambiente para Cinema!")
else:
  print("Não encontrado, escolha dentre as opções acima")


if opcao == "1":
  configuracoes = {"Iluminação": "alta", "Temperatura": "21ºC", "Som": "Silencioso"}
elif opcao == "2":
  configuracoes = {"Iluminação": "0%", "Temperatura": "20ºC", "Som": "Silencioso"}
elif opcao == "3":
  configuracoes = {"Iluminação": "80%", "Temperatura": "23ºC", "Som": "Música ambiente"}                
elif opcao == "4":
  configuracoes = {"Iluminação": "10%", "Temperatura": "20ºC", "Som": "Música baixo"}
elif opcao == "5":
  configuracoes = {"Iluminação": "0%", "Temperatura": "20ºC", "Som": "Alto"}
else:
  print("Não encontrado")
