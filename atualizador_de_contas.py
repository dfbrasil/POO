from heranca import Conta, ContaPoupanca, ContaCorrente, Cliente
from banco2 import Banco
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

    adc = AtualizadorDeContas(0.01, 1000)

    # adc.roda(c)
    # adc.roda(cc)
    # adc.roda(cp)

    # print(f'Saldo total: {adc.saldo_total}')
    b1 = Banco(numero=0, titular='', nome_tipo='', saldo=0, limite=1000)
    b1.adiciona()
    print(b1.pega_total_de_contas())
    print (b1.pega_conta())
   
    # tam = len)
    # print(tam)
    for i in range(len(b1.get_lista())):
        adc.roda(b1.get_lista[i])