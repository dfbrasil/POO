from nuisance import Nuisance
from insect import Insect


class Mosquito(Insect, Nuisance):
    
    def __init__(self, species):
        super().__init__(species)
        
    """método buzz"""
    def buzz(self):
        return super().get_species() + " buzzing around" 

    """método annoy"""
    def annoy(self):
        return "buzz buzz buzz"