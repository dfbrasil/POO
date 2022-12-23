from insect import Insect

class Butterfly(Insect):

    def __init__(self, species, colors, butterfly=None):
        super().__init__(species)
        self.__colors = colors

    """getters"""
    def get_colors(self):
        return self.__colors

    """setters"""
    def set_colors(self, new_colors):
        self.__colors = new_colors

    """str"""
    def __str__(self):
        return super().get_species() + "[" + self.__colors + "]" 
