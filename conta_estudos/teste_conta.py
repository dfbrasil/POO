
def cria_conta(numero, titular, saldo, limite):
    
    conta = {'numero':numero, 'titular':titular, 'saldo':saldo, 'limite':limite}
    return conta


def deposita (conta, valor):

    conta['saldo'] += valor


def saca(conta, valor):

    conta['saldo'] -= valor


def extrato(conta):

    print(f"número: {conta['numero']} e saldo: {conta['saldo']}")


# conta = cria_conta('123-7', 'João', 500.0, 1000.0)
# deposita(conta, 50.0)
# extrato(conta)

# saca(conta, 20.0)
# extrato(conta)

from conta import Conta

conta = Conta(123, 'Daniel', 1234, 1000)
# conta.titular = 'Daniel'
# conta.saldo = 123

# print (type(conta))
print(conta.titular)
print(conta.saldo)
