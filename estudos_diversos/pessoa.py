class Pessoa():

    def __init__(self, nome, idade_atual, peso_atual, altura, peso, anos):
        self.nome = nome
        self.idade_atual = idade_atual
        self.peso_atual = peso_atual
        self.altura = altura
        self.peso = peso
        self.anos = anos

    def envelhecer(self,anos):
        velho = self.idade_atual + anos
        return velho
   
    def engordar(self, peso):
        engordou = self.peso_atual + peso
        return engordou

    def emagrecer(self,peso):
            emagreceu = self.peso_atual + peso
            return emagreceu

    def crescer(self):
        if self.idade_atual <= 21:
            diferenca_idade = 21 - self.idade_atual
            alt = float(self.altura) + float(diferenca_idade * 0.5)
            return alt
        else:
            return self.altura

nome = input('Digite seu nome: ')
idade_atual = int(input('Digite a idade atual: '))
peso_atual = int(input('Digite o peso atual: '))
altura = int(input('Digite a altura atual: '))
anos = int(input('Digite quantos anos quer envelhecer? '))
peso = int(input('Quantos kgs vc quer alterar de seu peso atual?'))

pessoa = Pessoa(nome,idade_atual,peso_atual,altura, peso, anos)

print (f' {nome} envelheceu e está com {pessoa.envelhecer(anos)} anos')

if peso >0:
    print (f' {nome} engordou e está com {pessoa.engordar(peso)} kg')
elif peso < 0: 
    print (f' {nome} emagreceu e está com {pessoa.emagrecer(peso)} kg')
else:
    print(f' {nome} não alterou o peso')

print (f' A altura atual de {nome} é {pessoa.crescer()}')
