from insect import Insect


class Mosquito(Insect):

    """
    Método Construtor
    """

    def __init__(self, species):
        super().__init__(species)


    def buzz(self):
        print(f'{super().get_species()} buzzing around')

    """ 
    Método que é implementado pelo método abstrato nuisance.Nuisance
    """
    def annoy(self):
        print (f'buzz buzz buzz')
    
