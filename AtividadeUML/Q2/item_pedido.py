from produto import Produto


class ItemPedido:

        def __init__(self, produto:Produto, quantidade: int) -> None:
            self.produto = produto
            self.__quantidade = quantidade

        def get__quantidade(self):
            return self.__quantidade

        def set_quatidade(self, quantidade):
            self.__quantidade = quantidade

        def __str__(self) -> str:
            return (f'código: {self.produto.get_codigo()}, valor: {self.produto.get_valor()}, qtd: {self.__quantidade}')