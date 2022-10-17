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
        
        if (conta_saque == self.conta1.numero):
            temsaldo = self.saca()
            if temsaldo == True:
                conta_deposito.depositar(valor_trans)
            else:
                print (f'sem saldo em {self.conta1.numero}')
        
        elif (conta_saque == self.conta2.numero):
            temsaldo = self.saca()
            if temsaldo == True:
                conta_deposito.depositar(valor_trans)
            else:
                print (f'sem saldo em {self.conta2.numero}')


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
            conta1.extrato(qual_conta)

        elif operacao ==2:
            depositar1 = float(input('Digite um valor a ser depositado na primeira conta: '))
            conta1.depositar(depositar1)

        elif operacao == 3:
            saca1 = float(input('Digite um valor a ser sacado da primeira conta: '))
            print(conta1.saca(saca1))

        elif operacao == 4:

            conta_saque = int(input('Conta a ser realizada o saque : '))
            conta_deposito = int(input('Conta a ser realizada o deposito : '))
            valor = float(input('Digite um valor a ser transferido: '))

            if (conta_saque != numero1) or (conta_saque != numero2):
                print ('Conta inválida')

            else:
                valor_trans = float(input('Valor da transferencia: ')) 
                conta1.transferir(valor,conta2)

    # elif qual_conta == numero2:

    #     print ('1 - Para extrato')
    #     print ('2 - Para depositar')
    #     print ('3 - Para sacar')
    #     print ('4 - Para transferir')
    #     print ('0 - Para sair')
    #     operacao = int(input('Digite a operação que deseja fazer: '))

    #     if operacao > 4 or operacao < 0:
    #         print ('operação inválida')

    #     elif operacao == 1:
    #         conta2.extrato(numero2, saldo2)
        
    #     elif operacao ==2:
    #         depositar2 = float(input('Digite um valor a ser depositado na segunda conta: '))
    #         conta2.depositar(depositar2)

    #     elif operacao == 3:
    #         saca2 = float(input('Digite um valor a ser sacado da segunda conta: '))
    #         print(conta2.saca(saca2))
        
    #     elif operacao == 4:
    #         conta_trans = int(input('Conta a ser realizada a transferência: '))

    #         if conta_trans != numero1:
    #             print ('Conta inválida')

    #         else:
    #             valor_trans = float(input('Valor da transferencia: ')) 
    #             conta2.transferir21(valor_trans)
        
    else:
        print ('Conta inválida')
        operacao = int(input('Digite 0 para sair: '))

        