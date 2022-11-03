
import datetime

class Jogador:

    def __init__(self, nome, posicao, ano, mes, dia, nacionalidade, altura, peso):

        self.__nome = nome
        self.__posicao = posicao
        self.__data_nascimento = datetime.datetime(ano, mes, dia)
        self.__nacionalidade = nacionalidade
        self.__altura = altura
        self.__peso = peso

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

    def get_posicao(self):
        return self.__posicao
    
    def set_posicao(self, posicao):
        self.__posicao = posicao

    def get_data_nascimento(self):
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def get_nacionalidade(self):
        return self.__nacionalidade

    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura):
        self.__altura = altura

    def get_peso(self):
        return self.__peso

    def set_peso(self,peso):
        self.__peso = peso

    

