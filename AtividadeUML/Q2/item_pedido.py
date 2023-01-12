from produto import Produto


class ItemPedido:

        def __init__(self, produto:Produto, quantidade: int) -> None:
            self.__produto = produto
            self.__quantidade = quantidade

        def get_quantidade(self):
            return self.__quantidade

        def set_quantidade(self, quantidade):
            self.__quantidade = quantidade

        def get_produto(self):
            return self.__produto

        def set_produto(self, produto):
            self.__produto = produto

        def __str__(self) -> str:
            return (f'código: {self.produto.get_codigo()}, valor: {self.produto.get_valor()}, qtd: {self.__quantidade}')