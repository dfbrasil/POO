from jogador import Jogador

nome = input('Digite o nome do Jogador: ')
posicao = input('Digite a posição do Jogador: ')
ano = int(input('Digite o ano de nascimento do Jogador: ')) 
mes = int(input('Digite o mês de nascimento do Jogador: ')) 
dia = int(input('Digite o dia de nascimento do Jogador: '))
nacionalidade = input('Digite a nacionalidade do Jogador: ')
altura = float(input('Digite a altura do Jogador: '))
peso = float(input('Digite o peso de nascimento do Jogador: '))


player = Jogador(nome,posicao,ano,mes,dia,nacionalidade,altura,peso)

player.imprime()
player.idade()
player.aposentadoria()