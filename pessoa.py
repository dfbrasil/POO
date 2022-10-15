class Pessoa():

    def __init__(self, nome, idade_atual, peso_atual, altura, peso_futuro, idade_futuro):
        self.nome = nome
        self.idade_atual = idade_atual
        self.peso_atual = peso_atual
        self.altura = altura
        self.peso_futuro = peso_futuro
        self.idade_futuro = idade_futuro

    def envelhecer(self):

        velho = self.idade_futuro - self.idade_atual
        return velho
   
    def engordar(self):
        if self.peso_atual < self.peso_futuro:
            engordou = self.peso_futuro - self.peso_atual
            return engordou

    def emagrecer(self):
        if self.peso_atual > self.peso_futuro:
            emagreceu = self.peso_atual - self.peso_futuro
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
idade_futuro = int(input('Digite a idade futura: '))
peso_futuro = int(input('Digite o peso futuro: '))

pessoa = Pessoa(nome,idade_atual,peso_atual,altura, peso_futuro, idade_futuro)

print (f' {nome} envelheceu {pessoa.envelhecer()} anos')
print (f' {nome} engordou {pessoa.engordar()} kg')
print (f' {nome} emagreceu {pessoa.emagrecer()} kg')
print (f' A altura atual de {nome} é {pessoa.crescer()}')
