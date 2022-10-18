from datetime import date

class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:

    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura


    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print (f'cliente: {self.titular.nome} {self.titular.sobrenome}\nnúmero: {self.numero} \nsaldo: {self.saldo} \ndata de criação da conta {chamaHora(data)}' )

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True
    

class DataBanco:

    def __init__(self):
        data = date.today()
        self.data = data

    def chamaHora(data):

        print("Data da criaçã da conta: ", data) 

