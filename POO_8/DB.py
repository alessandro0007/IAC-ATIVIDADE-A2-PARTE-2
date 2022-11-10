from livro import livro
from pessoa import pessoa
from emprestimo import emprestimo

class BD:
    lista_pessoa = []
    lista_emprestimo = []

    estoque_livro = []
    def gerar_BD(self):
        self.estoque_livro.append(livro(1, "harry potter e a pedra filosofal", "J.K. Rowling", "Fantasia", 1997, 2))
        self.estoque_livro.append(livro(2, "harry potter e a camara secreta", "J.K. Rowling", "Fantasia", 1998, 3))
        self.estoque_livro.append(livro(3, "harry potter e o prisioneiro de azkaban", "J.K. Rowling", "Fantasia", 2000, 2))
        self.estoque_livro.append(livro(4, "harry potter e o calice de fogo", "J.K. Rowling", "Fantasia", 1999, 2))
        self.estoque_livro.append(livro(5, "harry potter e a ordem da fenix", "J.K. Rowling", "Fantasia", 2003, 2))
        self.estoque_livro.append(livro(6, "harry potter e o  enigma do principe", "J.K. Rowling", "Fantasia", 2005, 2))
        self.estoque_livro.append(livro(7, "harry potter e as reliqueas da morte", "J.K. Rowling", "Fantasia", 2007, 2))

    def emprestar(self, nome, telefone, livro, data_emprestimo, data_devolucao):
        for item in self.estoque_livro:
            if(item.codigo == livro):
                self.lista_pessoa.append(pessoa(nome, telefone))
                self.lista_emprestimo.append(emprestimo(livro, nome, data_emprestimo, data_devolucao))
                print("Empréstimo realizado com sucesso!")
                return
        print("Código não encontrado!")


    def devolucao(self, nome, codigo_livro):
        if len(self.lista_emprestimo) != 0:
            cont = 0
            for item in self.lista_emprestimo:
                if item.codigo_livro == codigo_livro and item.nome_pessoa == nome:
                    self.lista_emprestimo.pop(cont)
                    return "Devolução feita com sucesso!".format(nome)
                else:
                    return "Empréstimo não encontrado!"

    def estoque(self, codigo):
        for item in self.estoque_livro:
            if(item.codigo == codigo and item.qtd >= 1):
                return True

        return False



    def remove_estoque(self, codigo):
        for item in self.estoque_livro:
            if (item.codigo == codigo):
                item.qtd = item.qtd - 1

    def devolve_estoque(self, codigo):
        for item in self.estoque_livro:
            if (item.codigo == codigo):
                item.qtd = item.qtd + 1