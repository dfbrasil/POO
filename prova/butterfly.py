from insect import Insect


class Butterfly(Insect):
    """
    Método Construtor
    """
    def __init__(self, species, colors, butterfly=None):
        super().__init__(species)


    def toString(self, lista_cores):
       
        if len(lista_cores) == 0:
            print (f'{super().get_species()}')
        
        elif len(lista_cores) == 1:
            print (f'{super().get_species()} {lista_cores[0]}')
        
        elif len(lista_cores) == 2:
            print (f'{super().get_species()} {lista_cores[0]} e {lista_cores[1]}')

        else:
            for cor in lista_cores:
                print (f'{super().get_species()} possui a cor: {cor}')
    