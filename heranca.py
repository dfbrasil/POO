from datetime import date

class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        
        
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Realizado depósito de R${valor}. ')

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'Realizado saque de R${valor}. ')

    def extrato(self):
        print (f'cliente: {self.titular.nome} {self.titular.sobrenome}\nnúmero: {self.numero} \nsaldo: {self.saldo} \ndata de criação da conta {DataBanco.chamaHora()}' )
        self.historico.transacoes.append(f'Solicitado extrato, com saldo de R${self.saldo}')

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'Realizada transferencia de R${valor} para conta {destino.numero}')
            return True

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa
        return self.saldo

    def __str__(self):
        return f'Dados da conta: \nNúmero: {self.numero} \nTitular: {self.titular} \nSaldo: {self.saldo} \nLimite: {self.limite}'


class ContaCorrente(Conta):
    
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 2
        return self.saldo

    def deposita(self, valor):
        self.saldo += valor - 0.10

class ContaPoupanca(Conta):
    
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 3
        return self.saldo


class DataBanco:

    def chamaHora():
        data = date.today()
        return data


class Historico:

    def __init__(self):
        self.transacoes = []


    def imprime(self):
        print("transações: ")
        for t in self.transacoes:
            print("-", t)


#Questão 2 (Opcional)
#Não, pois atualiza já estaria implementada envolvendo apenas o valor de saldo total.
