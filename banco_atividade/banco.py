from collections import defaultdict

from heranca1 import Conta


class Variaveis(Conta):
    def __init__(self, numero, titular, nome_tipo, saldo, limite):
        super().__init__(numero, titular, nome_tipo, saldo, limite )


class Banco(Conta):

    def __init__(self, numero, titular, nome_tipo, saldo, limite  ):
        super().__init__(numero, titular, nome_tipo, saldo,  limite)
        self.lista_usuario = []
        self.lista = []

    def adiciona(self):

        opcao = 1
    
        while opcao != 0:
            num1 =  input('Digite conta: ')
            tit1 =  input('Digite nome: ')
            tip1 =  input('Digite tipo: ')
            sal1 = int(input('Digite saldo: '))
            lim1 = int(input ('Digite o limite: '))
            self.lista_usuario = Variaveis(num1, tit1, tip1, sal1, lim1)
            self.lista.append(self.lista_usuario)
            opcao = int(input('Digite 0 para sair: '))

        for tits in range(len(self.lista)):        
            return self.lista[tits]


    def pega_conta(self):
        n = int(input('Digite a posição da conta: '))
        for i in range(len(self.lista)):
            conta = self.lista[n]
        return conta


    def pega_total_de_contas(self):
        tam = len(self.lista)
        return tam


    def get_lista(self):
        return (self.lista)
