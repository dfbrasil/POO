from nuisance import Nuisance
from person import Person


class Telemarketing (Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    
    def giveSalesPitch(self):
        print (f'{super().get_name()}  pressiona os outros a comprar coisas')
    
    """ 
    Método que é implementado pelo método abstrato nuisance.Nuisance
    """
    def annoy(self):
        print (f'{super().get_name()} irrita ao dar um discurso de vendas.')