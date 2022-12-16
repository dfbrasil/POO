from datetime import date

from manipulador_de_tributaveis import ManipuladorDeTributaveis
from tributavel import Tributavel


class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:

    def __init__(self, numero, titular, nome_tipo, saldo, limite = 1000):
        self.numero = numero
        self.titular = titular
        self.nome_tipo = nome_tipo
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
        return f'Dados da conta: \nNúmero: {self.numero} \nTitular: {self.titular} \nTipo da conta: {self.nome_tipo} \nSaldo: {self.saldo} \nLimite: {self.limite}'


class ContaCorrente(Conta):#se herdar de Tributável será uma herança multipla e não uma interface
    
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 2
        return self.saldo

    def deposita(self, valor):
        self.saldo += valor - 0.10

    def get_valor_imposto(self):
        return self.saldo * 0.01

class ContaPoupanca(Conta):
    
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 3
        return self.saldo

class SeguroDeVida:

    def __init__(self, valor, titular, numero_apolice):
        self.valor = valor
        self.titular = titular
        self.numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self.valor * 0.05


class ContaInvestimento(Conta, Tributavel): #herdando tributável obrigado a implementar o método get_valor_imposto

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 5

    def get_valor_imposto(self):
        return self.saldo * 0.03



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



if __name__ == '__main__':
    from tributavel import Tributavel

    cc = ContaCorrente('João', '123-4',nome_tipo='',saldo=0)
    cc.deposita(1000.0)

    seguro = SeguroDeVida(100.0, 'José', '345-77')

    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida) #só registra se não tiver herdado na classe Tributavel

    lista_tributaveis = []
    lista_tributaveis.append(cc)
    lista_tributaveis.append(seguro)

    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    print(total)

    cp = ContaPoupanca('123-6', 'Maria',nome_tipo='',saldo=0)
    lista_tributaveis.append(cp)

    total = mt.calcula_impostos(lista_tributaveis)
    print(total)

    ci = ContaInvestimento('Ana', '123-0',nome_tipo='',saldo=0)
    ci.deposita(100.0)
    Tributavel.register(ContaInvestimento)

    lista_tributaveis.append(ci)
    mt = ManipuladorDeTributaveis()

    total = mt.calcula_impostos(lista_tributaveis)
    print(total)