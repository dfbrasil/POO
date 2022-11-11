from data import Data

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

data_teste = Data(dia, mes, ano)
d1 = data_teste

# d2 = Data(15,1,2000) #insira uma data para soma à data inicial

d2 = int(input('Digite uma quantidade de dias a ser somada à data:'))

d3 = d1 + d2

print (f'Data inicial {data_teste.__str__()}')

verifica_bissexto = int(input('Digite um ano para verificar se é bissexto: '))

data_teste.bissexto(verifica_bissexto)

data_teste.avanca(dia,mes,ano)

print (f'Avançando um dia à data inicial: {data_teste.__str__()}')

print (f'Impriminto a data somada a quantidade de dias desejada: {d3.__str__()}')

