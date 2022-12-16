from pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, idade, codigo):
        super().__init__(nome, sobrenome, idade)
        self.__codigo = codigo

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def metodo_abstrato(self):
        return self.__codigo
