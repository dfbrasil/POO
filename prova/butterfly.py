from insect import Insect


class Butterfly(Insect):
    """
    Método Construtor
    """
    def __init__(self, species, colors, butterfly=None):
        super().__init__(species)
        self.__species = species
        self.__colors = colors
        self.__butterfly = butterfly

    def toString(self, lista_cores):
       
        if len(lista_cores) == 0:
            print (f'{self.__species}')
        
        elif len(lista_cores) == 1:
            print (f'{self.__species} {lista_cores[0]}')
        
        elif len(lista_cores) == 2:
            print (f'{self.__species} {lista_cores[0]} e {lista_cores[1]}')

        else:
            for cor in lista_cores:
                print (f'{self.__species} possui a cor: {cor}')
    