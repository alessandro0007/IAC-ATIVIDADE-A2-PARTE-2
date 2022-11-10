class Pagamento:
    forma_pagamento = []

    def cria_pagamento(self):

        self.forma_pagamento.append(codigo_pagamento(1, "Dinheiro"))
        self.forma_pagamento.append(codigo_pagamento(3, "Cartão"))

class codigo_pagamento:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome