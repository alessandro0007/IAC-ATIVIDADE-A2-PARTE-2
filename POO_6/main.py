from Pagamento import Pagamento
from Compra import pedido
from DB import DB



DB = DB()
DB.criar_estoque()
Compra = pedido()
Pagamento = Pagamento()
Pagamento.cria_pagamento()


opcao = 3
while (opcao !=2):
    for item in DB.estoque_produtos:
        if (item.quantidade > 0):
            print(f"Código do item: {item.codigo}. Produto: {item.nome}. Valor da unidade: R${item.preco:.2f}. Quantidade em estoque: {item.quantidade}")
    selecionado = int(input("Digite o código do produto:"))
    Quantidade = int(input("Digite a quantidade do produto:"))

    if (DB.verifica_estoque(selecionado, Quantidade)):
        pedido.adicionarLista(selecionado, Quantidade)
        DB.remover_estoque(selecionado, Quantidade)
    else:
        print("Não possui quantidade disponível no estoque.")
    print("1. Continuar comprando")
    print("2. Finalizar Compra")
    opcao = int(input("Digite a opção:"))

for item in Pagamento.forma_pagamento:
    print(f"{item.codigo}. {item.nome}. ")
    pagamento_Selecionado = int(input("Seleciona a forma de pagamento: "))

if (pagamento_Selecionado == 1 or pagamento_Selecionado == 2 or pagamento_Selecionado == 3):
    print("Pagamento realizado com sucesso!")
else:
    print("Pagamento não aprovado!")
