
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    """
    Métodos Gets and Sets
    """

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def verifica(self, age):

        if (age >= 1) and (age <= 150 ):
            self.__age = age
        else:
           self.set_name(str(f'Idade inválida, {self.get_name()} precisa ter entre 1 e 150 anos'))

    def __str__(self):
        return (f'{self.get_name()} {self.get_age()}')


