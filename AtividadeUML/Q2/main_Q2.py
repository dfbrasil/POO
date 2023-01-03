from item_pedido import ItemPedido
from produto import Produto
from pedido import Pedido


produto1 = Produto(1,1.0,'prod1')
produto2 = Produto(2,2.0,'prod2')
produto3 = Produto(3,3.0,'prod3')

item_pedido1 = ItemPedido(produto1,5)
item_pedido2 = ItemPedido(produto2,10)
item_pedido3 = ItemPedido(produto3,20)

pedido = Pedido(0)

pedido.adicionar_item(item_pedido1)
pedido.adicionar_item(item_pedido2)
pedido.adicionar_item(item_pedido3)

valor = (pedido.obter_total())
pedido.set_valor_total(valor)
print(pedido.get_valor_total())
