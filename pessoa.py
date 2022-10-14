class Pessoa():

    def __init__(self, nome, idade_atual, peso_atual, altura, peso_futuro, idade_futuro):
        self.nome = nome
        self.idade_atual = idade_atual
        self.peso_atual = peso_atual
        self.altura = altura
        self.peso_futuro = peso_futuro
        self.idade_futuro = idade_futuro


    def envelhecer(self, idade_atual, idade_futuro):

        velho = self.idade_futuro - self.idade_atual

        return velho

   
    def engordar(self, peso_atual, peso_futuro):
        if self.peso_atual < self.peso_futuro:
            engordou = self.peso_futuro - self.peso_atual
            return engordou


    def emagrecer(self,peso_atual, peso_futuro):
        if self.peso_atual > self.peso_futuro:
            emagreceu = self.peso_atual - self.peso_futuro
            return emagreceu

 
    def crescer(self, idade_atual, idade_futuro, peso_atual, altura):
        if idade_atual < 21:
            diferenca_idade = self.envelhecer(idade_atual, idade_futuro)
            alt = float(self.altura) + float(diferenca_idade * 0.5)
            return alt
        else:
            return self.altura


nome = input('digite seu nome')
idade_atual = int(input('digite a idade atual'))
peso_atual = int(input('digite o peso atual'))
altura = int(input('digite a altura atual'))
idade_futuro = int(input('digite a idade futura'))
peso_futuro = int(input('digite o peso futuro'))

pessoa = Pessoa(nome,idade_atual,peso_atual,altura, peso_futuro, idade_futuro)

print (pessoa.nome)
print (pessoa.idade_atual)
print (pessoa.peso_atual)
print (pessoa.altura)


print (f'envelheceu {pessoa.envelhecer(idade_atual, idade_futuro)} anos')
print (f' engordou {pessoa.engordar(peso_atual, peso_futuro)} kg')
print (f' emagreceu {pessoa.emagrecer(peso_atual, peso_futuro)} kg')
print (f' a altura atual é {pessoa.crescer(idade_atual, idade_futuro, peso_atual, altura)}')

