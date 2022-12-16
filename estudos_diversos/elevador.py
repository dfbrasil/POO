
class Elevador:

    def __init__(self, capacidade, andares, num_pessoas, andar_atual):
        self.__capacidade = capacidade
        self.__andares = andares
        self.__num_pessoas= num_pessoas
        self.__andar_atual = andar_atual

    def get_capacidade(self):
        return self.__capacidade
    
    def set_capacidade(self,capacidade):
        self.__capacidade = capacidade

    def get_andares(self):
        return self.__andares

    def set_andares(self, andares):
        self.__andares = andares
    
    def get_num_pessoas(self):
        return print(f'Existe(m) {self.__num_pessoas} pessoas no elevador')

    def set_andare(self, num_pessoas):
        self.__num_pessoas = num_pessoas

    def get_andar_atual(self):
        return print(f' Estamos no andar {self.__andar_atual}')

    def set_andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual
    

    def entrar(self, capacidade):

        if self.__num_pessoas >= capacidade:
            return print(f'Não é permitido entrar, elevador lotado com {self.__capacidade} pessoas')
        else:
            self.__num_pessoas += 1
            return self.__num_pessoas


    def sair(self, capacidade):

        if self.__num_pessoas <= 0:
            return print(f'Não é possível sair, elevador vazio')
        else:
            self.__num_pessoas -= 1
            return self.__num_pessoas


    def subir(self, andar_atual):

        if self.__andar_atual == self.__andares:
            return print (f'Não é possível subir, já estamos no último andar')
        
        else:
            self.__andar_atual += 1
            return self.__andar_atual
    

    def descer(self, andar_atual):

        if self.__andar_atual == 0:
            return print (f'Não é possível descer, já estamos no térreo')
        
        else:
            self.__andar_atual -= 1
            return self.__andar_atual