from insect import Insect

class Butterfly(Insect):
    def __init__(self, species, colors, butterfly=None):

        super().__init__(species)
        if butterfly == None:
            self.__colors = colors
            self.__butterfly = butterfly
        else:
            self.__colors = butterfly.get_colors()
            self.__butterfly = butterfly.get_butterfly()

    def __str__(self):
        return f"{self.get_species()}{self.__colors}"

    def get_colors(self):
        return self.__colors

    def set_colors(self, colors):
        self.__colors = colors

    def get_butterfly(self):
        return self.__butterfly

    def set_butterfly(self, butterfly):
        self.__butterfly = butterfly