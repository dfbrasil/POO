
import datetime


class Jogador:

    def __init__(self, nome, posicao, ano, mes, dia, nacionalidade, altura, peso):

        self.__nome = nome
        self.__posicao = posicao
        self.__data_nascimento = datetime.date(ano, mes, dia)
        self.__nacionalidade = nacionalidade
        self.__altura = altura
        self.__peso = peso

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

    def get_posicao(self):
        return self.__posicao
    
    def set_posicao(self, posicao):
        self.__posicao = posicao

    def get_data_nascimento(self):
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    
    def get_nacionalidade(self):
        return self.__nacionalidade

    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura):
        self.__altura = altura

    def get_peso(self):
        return self.__peso

    def set_peso(self,peso):
        self.__peso = peso

    def imprime(self):
        print('Nome:')
        print(self.__nome)
        print('Posição:')
        print(self.__posicao)
        print('Data de Nascimento:')
        print(self.__data_nascimento)
        print('Nascionalidade:')
        print(self.__nacionalidade)
        print('Altura:')
        print(self.__altura)
        print('Peso:')
        print(self.__peso)

    def idade(self):
        hoje = datetime.datetime.now()
        hoje_ano = hoje.year
        hoje_mes = hoje.month
        hoje_dia = hoje.day

        anos = hoje_ano - self.__data_nascimento.year

        if hoje_mes >= self.__data_nascimento.month:
            meses = hoje_mes - self.__data_nascimento.month
        else:
            meses = self.__data_nascimento.month - hoje_mes

        if hoje_dia >= self.__data_nascimento.day:
            dias = hoje_dia - self.__data_nascimento.day
        else:
            dias = self.__data_nascimento.day - hoje_dia

        return print(f'O jogador {self.__nome} tem {anos} anos, {meses} meses e {dias} dias de idade')

    def aposentadoria(self):
        hoje = datetime.datetime.now()
        hoje_ano = hoje.year
        anos = hoje_ano - self.__data_nascimento.year

        if self.__posicao == 'defesa':
            if anos <= 40:
                aposento = 40 - anos
                return print(f'Faltam {aposento} anos para o jogador {self.__nome} se aposentar')
            else:
                aposento = anos - 40
                return print(f'O jogador {self.__nome} já se aposentou fazem {aposento} anos')
        
        elif self.__posicao == 'meio-campo':
            if anos <= 38:
                aposento = 38 - anos
                return print(f'Faltam {aposento} anos para o jogador {self.__nome} se aposentar')
            else:
                aposento = anos - 38
                return print(f'O jogador {self.__nome} já se aposentou fazem {aposento} anos')
        
        elif self.__posicao == 'atacante':
            if anos <= 35:
                aposento = 35 - anos
                return print(f'Faltam {aposento} anos para o jogador {self.__nome} se aposentar')
            else:
                aposento = anos - 35
                return print(f'O jogador {self.__nome} já se aposentou fazem {aposento} anos')
