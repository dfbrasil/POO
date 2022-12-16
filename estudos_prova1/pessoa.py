
class Pessoa:

    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_sobrenome(self):
        return self.__sobrenome

    def set_sobrenome(self, nome):
        self.__sobrenome = nome    

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade
    
    def metodo_abstrato(self):
        pass

