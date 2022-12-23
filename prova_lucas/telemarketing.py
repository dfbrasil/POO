from person import Person

class Telemarketing(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    """método giveSalesPitch"""
    def giveSalesPitch(self):
        return f'{self.get_name()}  pressiona os outros a comprar coisas.'

    """método Annoy"""
    def annoy(self):
        return f'{self.get_name()} irrita ao dar um discurso de vendas.'