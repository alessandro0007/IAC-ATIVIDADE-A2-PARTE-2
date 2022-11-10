from Contatos import Contato


class agenda():
  def inserir(self, nome, telefone):
    return Contato(nome, telefone)

  def lista_numeros(self, lista_Telefone):
    for telefone in lista_Telefone:
      print(f"{telefone.nome} | {telefone.telefone}")


  def excluir_contato(self, lista_Telefone, nome):
    if len(lista_Telefone) != 0:
      cont = 0
      for telefone in lista_Telefone:
        if telefone.nome == nome:
          lista_Telefone.pop(cont)
          return f"Contado {nome} removido com sucesso!"
        else:
          return "Contato não encontrado!"
    else:
      return "Não há contatos salvosS!"