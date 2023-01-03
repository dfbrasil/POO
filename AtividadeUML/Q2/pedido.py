from item_pedido import ItemPedido
from produto import Produto

class Pedido:

    lista_pedido: ItemPedido = []

    def __init__(self, valor_total) -> None:
        self.__valor_total = valor_total

    def get_valor_total(self):
        return self.__valor_total

    def set_valor_total(self, valor):
        self.__valor_total = valor

    def adicionar_item(self, item:ItemPedido):
        self.lista_pedido.append(item)

    def obter_total(self):
        for i in self.lista_pedido:
            qtd = float(i.get__quantidade())
            vlr = float(i.produto.get_valor())
            valor_total = qtd * vlr
        return valor_total
