class pedido:
    def __init__(self):
        self.lista_itens = []
        self.forma_pagamento = ""

    def adicionar_lista(self,adicionado, quantidade):
        self.lista_itens.append(compra(adicionado, quantidade))
    def selecionar_pagamento(self, forma_pagamento):
        self.forma_pagamento = forma_pagamento

class compra:
    def __init__(self, item, quantidade):
        self.item = item
        self.quantidade = quantidade