from collections import defaultdict

dicio = defaultdict(list)

opcao = 1
while opcao != 0:
    nome = input('digite nome: ')
    conta = input('Digite conta:')
    tipo = input('Tipo: ')
    dicio['Nome'].append(nome)
    dicio['Conta'].append(conta)
    dicio['Tipo'].append(tipo)
    opcao = int(input('opção: '))


# dicio['nome'] = ['teste']
# dicio['conta'] = [123]
# dicio['nome'] = ['teste2']
# dicio['conta'] = [456]

print (dicio)