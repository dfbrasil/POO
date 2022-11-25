
"""Importação da função datetime"""
import datetime

"""Criação da classe Data"""
class Data:

    """ Construtor de inicalização dos atributos iniciais Dia, Mes, Ano"""
    def __init__(self, dia = datetime.date.today().day, mes = datetime.date.today().month, ano = datetime.date.today().year):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    """Método que retorna o parâmetro privado __dia"""
    def get_dia(self):
        return self.__dia

    """Método que altera o parâmetro privado __dia"""
    def set_dia(self, dia):
        self.__dia = dia

    """Método que retorna o parâmetro privado __mes"""
    def get_mes(self):
        return self.__mes

    """Método que altera o parâmetro privado __mes"""
    def set_mes(self, mes):
        self.__mes = mes

    """Método que retorna o parâmetro privado __ano"""
    def get_ano(self):
        return self.__ano

    """Método que altera o parâmetro privado __ano"""
    def set_ano(self,ano):
        self._ano = ano

    """Método que verifica se o ano é bissexto"""    
    def bissexto(self, ano):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano%400==0):
            print(f'{ano} é um ano bissexto !!')
        else:
            print(f'{ano} não é um ano é bissexto !!')

    '''Método que avança mais um dia e verifica as condições para isso'''
    def avanca(self, dia, mes, ano):
        if mes in (1,3,5,7,8,10,12) and dia < 30:
            self.__dia += 1
        elif mes in (1,3,5,7,8,10,12) and dia == 31:
            self.__dia = 1
            if mes == 12:
                self.__mes = 1
                self.__ano += 1
            else:
                self.__mes += 1

        elif (mes == 2) and ((ano % 4 == 0 and ano % 100 != 0) or (ano%400==0)) and dia == 28:
            self.__dia =+ 1
        
        elif (mes == 2) and ((ano % 4 == 0 and ano % 100 != 0) or (ano%400==0)) and dia == 29:
            self.__dia = 1
            self.__mes += 1

        elif (mes == 2) and dia == 27:
            self.__dia =+ 1

        elif (mes == 2)  and dia == 28:
            self.__dia = 1
            self.__mes += 1

        elif mes in (4,6,9,11) and dia < 30:
            self.__dia +=1
        
        elif mes in (4,6,9,11) and dia == 30:
            self.__dia = 1
            self.__mes += 1

    '''Método que soma um valor em dias à uma data, ou soma duas datas passadas pelo usuário'''
    def __add__(self, other):

        if (type(other) is not int):

            soma_dia = self.__dia + other.__dia
            soma_mes = self.__mes + other.__mes
            soma_ano = self.__ano + other.__ano

            self.__dia = soma_dia
            self.__mes = soma_mes
            self.__ano = soma_ano

        elif (type(other) is int):
            if self.__mes in (1,3,5,7,8,10,12) and ((self.__dia + other) <= 31):
                self.__dia += other
                
                return Data(self.__dia, self.__mes, self.__ano)

            elif self.__mes in (1,3,5,7,8,10,12) and ((self.__dia + other) > 31):

                dias_cheio = self.__dia + other
                dias_excesso = dias_cheio - 31
                self.__dia = dias_excesso
                if self.__mes == 12:
                    self.__mes = 1
                    self.__ano += 1
                else:
                    self.__mes += 1

                    return Data(self.__dia, self.__mes, self.__ano)

            elif (self.__mes == 2) and ((self.__ano % 4 == 0 and self.__ano % 100 != 0) or (self.__ano%400==0)) and ((self.__dia + other) <= 29):
                self.__dia =+ other

                return Data(self.__dia, self.__mes, self.__ano)
                
            elif (self.__mes == 2) and ((self.__ano % 4 == 0 and self.__ano % 100 != 0) or (self.__ano%400==0)) and ((self.__dia + other) > 29):
                dias_cheio = self.__dia + other
                dias_excesso = dias_cheio - 29
                self.__dia = dias_excesso
                self.__mes += 1

                return Data(self.__dia, self.__mes, self.__ano)

            elif (self.__mes == 2) and ((self.self.__dia + other) <= 28):
                self.__dia =+ other

                return Data(self.__dia, self.__mes, self.__ano)

            elif (self.__mes == 2)  and ((self.self.__dia + other) > 28):
                dias_cheio = self.__dia + other
                dias_excesso = dias_cheio - 28
                self.__dia = dias_excesso
                self.__mes += 1

                return Data(self.__dia, self.__mes, self.__ano)

            elif self.__mes in (4,6,9,11) and self.__dia ((self.self.__dia + other) <= 30):
                self.__dia += other

                return Data(self.__dia, self.__mes, self.__ano)
                
            elif self.__mes in (4,6,9,11) and ((self.self.__dia + other) > 29):
                dias_cheio = self.__dia + other
                dias_excesso = dias_cheio - 29
                self.__dia = dias_excesso
                self.__mes += 1

                return Data(self.__dia, self.__mes, self.__ano)

    '''Método que retorna a data'''
    def __str__(self):
        return (f'{self.__dia}/{self.__mes}/{self.__ano}')
