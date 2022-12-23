class Insect:

    def __init__(self, species):
        self.__species = species
    
    """getters"""
    def get_species(self):
        return self.__species

    """setters"""
    def set_species(self, new_species):
        self.__species = new_species

    """str"""
    def __str__(self):
        return "Insect: " + self.__species