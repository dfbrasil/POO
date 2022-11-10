# Crie uma classe para representar datas. Represente uma data usando três atributos privados: o dia, o mês, e o ano.


#   * Sua classe deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos. OK
#   * Caso as datas não sejam passadas no construtor (devem ser parâmetros opcionais), inicialize a data com a data atual fornecida pelo sistema operacional. Procure uma biblioteca que retorne a data atual do sistema operacional. 
# OK

#   * Forneça os métodos get/set para cada atributo. 
#OK

#   * Forneça o método __str__ para retornar uma representação da data como string. Considere que a data deve ser formatada mostrando o dia, o mês e o ano separados por barra (/).
#OK

#   * Forneça um método para avançar uma data para o dia seguinte. 
#   * Forneça um método para verificar se o ano é bissexto.
#OK
#   * Use o método __add__ para somar dois objetos da classe data. Além da soma de dois objetos do mesmo tipo,  o método deve permitir  a soma de uma "data" e um inteiro. Esse inteiro representa a quantidade de dias a ser somado.
#   * Use docstrings para documentar cada método.
#   * Escreva um programa de teste (main.py) separado da classe Data que demonstra as capacidades da classe.

import datetime


class Data:

    def __init__(self, dia = datetime.date.today().day, mes = datetime.date.today().month, ano = datetime.date.today().year):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        self.__dia = dia

    def get_mes(self):
        return self.__mes

    def set_mes(self, mes):
        self.__mes = mes

    def get_ano(self):
        return self.__ano

    def set_ano(self,ano):
        self._ano = ano
        
    def bissexto(self, ano):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano%400==0):
            print('Ano bissexto !!')
        else:
            print('Ano não é bissexto !!')

    def avanca(self, dia, mes, ano):
        if mes in (1,3,5,7,8,10,12) and dia < 30:
            self.__dia += 1
        #CONTINUA
            
        return


    def __str__(self):
        return (f'{self.__dia}/{self.__mes}/{self.__ano}')

    


# dia_atual = datetime.date.today().day
# mes_atual = datetime.date.today().month
# ano_atual = datetime.date.today().year
