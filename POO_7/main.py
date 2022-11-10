from Agenda import agenda

agenda = agenda()
lista_agenda = []

menu = 1
while (menu !=4):
  print("1 - Cadastrar contato.")
  print("2 - Listar todos os contatos.")
  print("3 - Apagar contato.")
  print("4 - Sair.")

  menu = int(input("Digite o número para uma das opções: "))

  if menu == 1:
    nome = input("Digite o nome:")
    telefone = int(input("Digite o telefone:"))
    lista_agenda.append(agenda.inserir(nome, telefone))

  elif menu == 2:
    agenda.lista_numeros(lista_agenda)

  elif menu == 3:
    nome = input("Digite o nome para a pesquisa:")
    print(agenda.excluir_contato(lista_agenda, nome))

  elif menu == 4:
    break
  else:
    print("Digite uma opção de 1 a 4!")
