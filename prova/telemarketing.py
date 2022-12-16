from nuisance import Nuisance
from person import Person


class Telemarketing (Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__name = name
        self.__age = age

    
    def giveSalesPitch(self,name_pich):
        print (f'{name_pich}  pressiona os outros a comprar coisas')
    
    """ 
    Método que é implementado pelo método abstrato nuisance.Nuisance
    """
    def annoy(self):
        print (f'{self.__name} irrita ao dar um discurso de vendas.')