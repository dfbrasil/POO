from unittest import removeResult


class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.idade = idade
        self. peso = peso
        self.altura = altura
        self.escolaridade = 'nenhuma'
        self.__historico = []

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.05
        self.idade +=1
    
    def engordar(self, kilos):
        self.peso += kilos

    def emagrecer(self, kilos):
        self.peso -= kilos
    
    def crescer (self, altura):
        self.altura += altura

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
        self.__historico.append(nome)

    def get_historico(self):
        return self.__historico

p = Pessoa("Daniel", 40, 70, 170)

print(p.get_nome())
p.set_nome('Teste')
print(p.get_nome())
