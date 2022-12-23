from insect import Insect

class Mosquito(Insect):
    def __init__(self, species):
        super().__init__(species)
    
    def buzz(self):
        return f"{self.get_species()} buzzing around."

    def annoy(self):
        return "buzz buzz buzz"
    
