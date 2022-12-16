from pessoa import Pessoa
from indentificador import Indentificador

class Cliente(Pessoa):

    def __init__(self,nome, sobrenome, idade, matricula):
        super().__init__(nome, sobrenome, idade)
        self.__matricula = matricula
        
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def metodo_abstrato(self):
        return self.__matricula
