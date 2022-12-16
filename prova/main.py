from butterfly import Butterfly
from friend import Friend
from hobby import Hobby
from insect import Insect
from moquisto import Mosquito
from nuisance import Nuisance
from person import Person
from telemarketing import Telemarketing

"""
Entradas da questão 1
"""
nome_person = input('Digite um nome: ')
idade_person = int(input('Digite uma idade: '))
pessoa = Person (nome_person, idade_person)
pessoa.verifica(idade_person)
print(pessoa)

"""
Entradas da questão 2
"""
hm = Hobby.music
hs = Hobby.sports
hg = Hobby.games
# h.print_my_hoby_is_games(h)

"""
Entradas da questão 3
"""
hob = input('Qual o hobby do amigo?')
idade_amigo = int(input('Qual a idade do amigo?'))
nome_amigo = input('Qual o nome do amigo?')
friend = Friend(nome_person, idade_amigo, hob)
friend.chill(nome_amigo)

lista_amigos = []
opcao = 1
while opcao != 0:
    opcao = int(input('Deseja adicionar um amigo? Digite 1 para inserir e 0 para sair: '))
    if opcao != 0:
        amigo = input('Digite o nome do amigo: ')
        lista_amigos.append(amigo)
    if opcao == 0:
        break

friend.play(lista_amigos, hm)

"""
Entradas da questão 4
"""

Nuisance.register(Telemarketing)

"""
Entradas da questão 5
"""
nome_pitch = input('Qual o nome do PicthMan?')
mkt = Telemarketing(nome_pitch, idade_person)
mkt.giveSalesPitch(nome_pitch)
mkt.annoy()

"""
Entradas da questão 7
"""

insect = input('Digite o nome da espécie de inseto: ')
inseto = Insect(insect)
print(inseto)

"""
Entradas da questão 6
"""

Nuisance.register(Mosquito)

mosq = Mosquito(insect)
mosq.annoy()
mosq.buzz()

"""
Entradas da questão 8
"""

lista_cores = []

opcao = 1
while opcao != 0:
    opcao = int(input('Deseja adicionar cor a espécie? Digite 1 para inserir e 0 para sair: '))
    if opcao != 0:
        cor = input('Digite o nome da cor para a especie: ')
        lista_cores.append(cor)
    if opcao == 0:
        break
butt = Butterfly(inseto,lista_cores)
butt.toString(lista_cores)

