from heranca import Conta, ContaPoupanca, ContaCorrente, Cliente
from banco import Banco

class AtualizadorDeContas:

    def __init__(self, selic, saldo_total):
        self.selic = selic
        self.saldo_total = saldo_total

    def roda(self, conta):
        print (f'Saldo da Conta: {conta.saldo}')
        self.saldo_total += conta.atualiza(self.selic)
        print(f'Saldo Final: {self.saldo_total}')

if __name__ == '__main__':
    # c = Conta('123-4', 'Joao', 1000.0)
    # cc = ContaCorrente('123-5', 'Jose', 1000.0)
    # cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    # adc = AtualizadorDeContas(0.01, 1000)

    b1 = Banco(dicio=dict)

    # adc.roda(c)
    # adc.roda(cc)
    # adc.roda(cp)

    b1.adiciona()
    b1.imprime()

    # print(f'Saldo total: {adc.saldo_total}')



    