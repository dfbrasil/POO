class Conta():
    
    def __init__(self, numero, titular, saldo, limite, nome_tipo, codigo_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.nome_tipo = nome_tipo
        self.codigo_tipo = codigo_tipo
       
    def depositar(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            return True
                
    def extrato (self, numero, saldo):
        print(f'numero {self.numero} saldo {self.saldo}')

    def transferir(self,conta_saque, conta_deposito, valor):


        print(f'saque {conta_saque} deposito {conta_deposito} valor{valor}')


        if (conta_saque == conta1.numero):
            temsaldo = conta1.saca(valor)
            if temsaldo == True:
                conta2.depositar(valor)
            else:
                print (f'sem saldo em {conta_saque}')

        else:
            temsaldo = conta2.saca(valor)
            if temsaldo == True:
                conta1.depositar(valor)
            else:
                print (f'sem saldo em {conta_saque}')


numero1 = int(input('Digite o número da primeira conta: '))
titular1 = (input('Digite o nome do titular primeira conta: '))
saldo1 = float(input('Digite o saldo da primeira conta: '))
limite1 = float(input('Digite o limite da primeira conta: '))
nome_tipo = input('Qual o nome da operação? Poupança ou Conta Corrente: ')
codigo_tipo = int(input('Qual o codigo da operação? 51 ou 03: '))

numero2 = int(input('Digite o número da segunda conta: '))
titular2 = (input('Digite o nome do titular segunda conta: '))
saldo2 = float(input('Digite o saldo da segunda conta: '))
limite2 = float(input('Digite o limite da segunda conta: '))
nome_tipo = input('Qual o nome da operação? Poupança ou Conta Corrente: ')
codigo_tipo = int(input('Qual o codigo da operação? 51 ou 03: '))

conta1 = Conta(numero1, titular1, saldo1, limite1, nome_tipo, codigo_tipo)
conta2 = Conta(numero2, titular2, saldo2, limite2, nome_tipo, codigo_tipo)

operacao = 1

while operacao != 0:

    qual_conta = int(input('Digite qual conta você deseja fazer as operações: '))

    if (qual_conta == numero1) or (qual_conta == numero2):

        print ('1 - Para extrato')
        print ('2 - Para depositar')
        print ('3 - Para sacar')
        print ('4 - Para transferir')
        print ('0 - Para sair')

        operacao = int(input('Digite a operação que deseja fazer: '))

        if operacao > 4 or operacao < 0:
            print ('operação inválida')

        elif operacao == 1:
            if qual_conta == numero1:
                conta1.extrato(numero1, saldo1)
            else:
                conta2.extrato(numero2, saldo2)

        elif operacao ==2:
            if qual_conta == numero1:
                depositar1 = float(input('Digite um valor a ser depositado na primeira conta: '))
                conta1.depositar(depositar1)
                
            else:
                depositar2 = float(input('Digite um valor a ser depositado na segunda conta: '))
                conta2.depositar(depositar2)

        elif operacao == 3:
            if qual_conta == numero1:
                saca1 = float(input('Digite um valor a ser sacado da primeira conta: '))
                conta1.saca(saca1)
            else:
                saca2 = float(input('Digite um valor a ser sacado da segunda conta: '))
                conta2.saca(saca2)

        elif operacao == 4:

            conta_deposito = int(input('Conta a ser realizada o deposito : '))
            valor = float(input('Digite um valor a ser transferido: '))

            if (conta_deposito == numero2):
                conta1.transferir(numero1, numero2, valor)
                
            elif (conta_deposito == numero1):
                conta2.transferir(numero2, numero1, valor)
                
            else: 
                print ('Conta inválida')

    else:
        print ('Conta inválida')
        operacao = int(input('Digite 0 para sair: '))

        