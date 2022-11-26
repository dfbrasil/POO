from collections import defaultdict

from heranca import Conta


class Nome(Conta):
   def __init__(self, titular, saldo):
        super().__init__(titular,saldo)

class Numero(Conta):
    def __init__(self,numero):
        super().__init__(numero)
        
class Tipo(Conta):
    def __init__(self, nome_tipo):
        super().__init__(nome_tipo)
        
class Saldo (Conta):
    def __init__(self,saldo):
        super().__init__(saldo)

class Banco(Conta):

    def __init__(self, numero, titular, saldo, limite=1000 ):
        super().__init__(numero, titular, saldo, limite)
        self.lista_titular = []
        self.lista_numero = []
        self.lista_tipo = []
        self.lista_saldo = []


    def adiciona(self):

        opcao = 1
    
        while opcao != 0:
            tit1 =  input('Digite nome: ')
            self.titular = Nome(tit1)
            num1 =  input('Digite conta: ')
            self.numero = Numero(num1)
            tip1 =  input('Digite tipo: ')
            self.tipo = Tipo(tip1)
            sal1 = input('Digite saldo: ')
            self.saldo = Saldo(sal1)
            self.lista_titular.append(self.titular)
            self.lista_numero.append(self.numero)
            self.lista_tipo.append(self.tipo)
            self.lista_saldo.append(self.saldo)
            opcao = int(input('Digite Opção: '))


        #Retornar 3 listas na mesma posição iterando com o FOR 
        
    def __str__(self):
        for tits in range(len(self.lista_titular), len(self.lista_numero), len(self.lista_tipo), len(self.lista_saldo) ):
            return self.lista_titular[tits], self.lista_numero[tits], self.lista_tipo[tits], self.lista_saldo[tits]

        

    def pega_conta(self):
        pass

    # def pega_total_de_contas(self, dicio):
    #     cont = 0
    #     for chave in self.dicio.keys():
    #         if dicio.chave == 'c':
    #             cont += 1
    #     return cont

    