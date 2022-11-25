from heranca import Conta, ContaCorrente, ContaPoupanca
from collections import defaultdict

class Banco(Conta):

    dicio = defaultdict(list)

    def __init__(self, dicio):
        self.dicio = dicio

    def adiciona(self):
        
        opcao = 1

        while opcao != 0 :
            print ('Bem-vindo ao Banco: \nPara inserir novas contas selecione uma das opções abaixo:')
            print ('1 - Adicionar Conta:')
            opcao = int(input('0 - Sair: '))

            if opcao == 1:
                op= 1
                while op != 0:
                    self.dicio = defaultdict(list)
                    nome = input('digite nome: ')
                    conta = input('Digite conta:')
                    tipo = input('Tipo: ')
                    self.dicio['Nome'].append(nome)
                    self.dicio['Conta'].append(conta)
                    self.dicio['Tipo'].append(tipo)
                    op = int(input('opção: '))

        return self.dicio
    
    def pega_conta(self):
        pass


    def pega_total_de_contas(self):
        pass

    def imprime(self):
        print(self.dicio)
