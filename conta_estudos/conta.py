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
    
    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
    
    def extrato(self):
        print (f'Número: {self.numero} \nSaldo: {self.saldo}')

    def transfere_para(self, destino, valor):
        if self.saldo >= valor:
            self.saca(valor)
            destino.saldo += valor
        else:
            print('Não há saldo')
        


cliente = Cliente('Brasil', 'Freitas', 123456)

conta = Conta(123, cliente, 1000)

conta.deposita(20.0)
conta.extrato()
conta.saca(15)
conta.extrato()
print (conta.limite)
print(conta.titular.sobrenome)

