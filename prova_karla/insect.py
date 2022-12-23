class Insect:
    def __init__(self, species):
        self.__species = species

    def __str__(self):
        return f"{__class__.__name__}:{self.__species}"

    def get_species(self):
        return self.__species

    def set_species(self, species):
        self.__species = species