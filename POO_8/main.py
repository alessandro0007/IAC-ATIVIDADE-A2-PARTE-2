from DB import BD
BD = BD()
BD.gerar_BD()
menu = 1
while (menu !=4):

  print("1 - Mostrar todos os livros")
  print("2 - Realizar Empréstimo")
  print("3 - Devolver livro.")
  print("4 - Sair.")
  menu = int(input("Digite a opção: "))

  if menu == 1:
      for item in BD.estoque_livro:
        print(f"Código do Livro: {item.codigo}. Livro: {item.nome}. Autor: {item.autor}. Gênero: {item.genero}. Ano: {item.ano}. Quantidade: {item.quantidade}")

  elif menu == 2:
      nome = input("Digite o nome:")
      telefone = int(input("Digite o telefone:"))
      codigo_livro = int(input("Digite o código do livro:"))
      data_emprestimo = (input("Digite a data do empréstimo:"))
      data_devolucao = (input("Digite a data que você irá devolver o livro:"))

      if (BD.estoque(codigo_livro)):
        BD.emprestar(nome, telefone, codigo_livro, data_emprestimo, data_devolucao)
        BD.retira_estoque(codigo_livro)
      else:
          print("Não possui quantidade disponível no estoque.")


  elif menu == 3:
      nome = input("Digite o nome para confirmar a devolução:")
      codigo_livro = int(input("Digite o código do livro:"))
      print(BD.devolucao(nome, codigo_livro))
      BD.devolver_estoque(codigo_livro)

  elif menu == 4:
      break
  else:
    print("Digite uma opção válida!")