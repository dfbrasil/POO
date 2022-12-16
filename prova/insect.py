

class Insect:

    """
    Método Construtor
    """
    def __init__(self, species):
        self.__species = species

    """
    Métodos Gets and Sets
    """
    def get_species(self):
        return self.__species

    def set_species (self, species):
        self.__species = species

    def __str__(self):
        return (f'Insect: {self.get_species()}')