from data import Data

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

data_teste = Data(dia, mes, ano)

print (data_teste.__str__())

verifica_bissexto = int(input('Digite um ano para verificar se é bissexto: '))

data_teste.bissexto(verifica_bissexto)



