import datetime

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:

    def __init__(self, numero, cliente, saldo, limite=1000):
        print('inicializado uma conta --> executando o __init__')
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de {valor} reais.')

    def saca(self, valor):
        self.saldo -= valor
        self.historico.transacoes.append(f'Saque de {valor} reais.')
    
    def extrato(self):
        print (f'Número: {self.numero} \nSaldo: {self.saldo}')
        self.historico.transacoes.append(f'Tirou extrato - saldo de {self.saldo}')

    def transfere_para(self, destino, valor):
        if self.saldo >= valor:
            self.saca(valor)
            destino.saldo += valor
            self.historico.transacoes.append(f'Transferência de {valor} para a conta {destino.numero}')
        else:
            print('Não há saldo')

class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print (f'Data de abertura: {self.data_abertura}')
        print ('Transações: ')

        for t in self.transacoes:
            print ('-', t)


cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1, 1000.0)
conta2 = Conta('123-5', cliente2, 1000.0)
conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transfere_para(conta2, 200.0)
conta1.extrato

conta1.historico.imprime()

conta2.deposita(200.0)
conta2.historico.imprime()
