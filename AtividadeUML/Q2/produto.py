
class Produto:

    def __init__(self, codigo:int, valor:float, descricao:str) -> None:
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao = descricao


    '''Métodos getters and setters'''
    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao