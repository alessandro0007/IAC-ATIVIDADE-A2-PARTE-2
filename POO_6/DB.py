from Mercadoria import produto

class DB:
    estoque_produtos = []
    def cria_estoque(self):
        self.estoque_produtos.append(produto(1, "uva",5.55, 90))
        self.estoque_produtos.append(produto(2, "morango", 10.90, 150))
        self.estoque_produtos.append(produto(3, "Arroz 5k", 20.90, 150))
        self.estoque_produtos.append(produto(4, "Arroz 1kg", 15.59, 140))
        self.estoque_produtos.append(produto(5, "Feijao 1kg", 6.50, 110))
        self.estoque_produtos.append(produto(6, "Chocolate", 6.80, 110))
        self.estoque_produtos.append(produto(9, "Papel higiênico", 12.50, 111))
        self.estoque_produtos.append(produto(10, "Shampoo", 7.65, 80))
        self.estoque_produtos.append(produto(11, "Sabonete", 1, 130))
        self.estoque_produtos.append(produto(12, "Sabonete Liquido 500ml", 12, 160))
        self.estoque_produtos.append(produto(13, "Condicionador", 13, 120))
        self.estoque_produtos.append(produto(14, "Creme Dental", 4.50, 160))
        self.estoque_produtos.append(produto(15, "Linguiça", 16.80, 150))
        self.estoque_produtos.append(produto(16, "Carne Bovina", 45.99, 160))
        self.estoque_produtos.append(produto(17, "Carne Suína", 23.50, 160))
        self.estoque_produtos.append(produto(18, "Macarrão", 15, 150))
        self.estoque_produtos.append(produto(19, "maça",7.50, 120))
        self.estoque_produtos.append(produto(20, "cerveja", 3.29, 350))


    def verifica_estoque(self, codigo, quantidade):
        for item in self.estoque_produtos:
            if(item.codigo == codigo and item.quantidade >= quantidade):
                return True

        return False

    def remover_estoque(self, codigo, quantidade):
        for item in self.estoque_produtos:
            if (item.codigo == codigo):
                item.quantidade = item.quantidade - quantidade