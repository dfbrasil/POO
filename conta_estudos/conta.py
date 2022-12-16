from historico import Historico

class Conta:

    def __init__(self, numero, cliente, saldo, limite=1000):
        # print('inicializado uma conta --> executando o __init__')
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
