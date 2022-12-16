from person import Person


class Friend(Person):

    """
    Método Construtor
    """
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.__hobby = hobby

    """
    Métodos Gets and Sets
    """
    def get_hobby(self):
        return self.__hobby

    def set_hobby(self, hobby):
        self.__hobby = hobby

    def chill(self,nome):
        print (f'{nome} is chilling')

    def play(self, lista_amigos, hobby):

        if len(lista_amigos) == 0:
            print (f'jogar {hobby}')
        
        elif len(lista_amigos) == 1:
            print (f'jogar {hobby} com {lista_amigos[0]}')
        
        elif len(lista_amigos) == 2:
            print (f'jogar {hobby} com {lista_amigos[0]} e {lista_amigos[1]}')

        else:
            for amigo in lista_amigos:
                print (f'jogando {hobby} com {amigo}')
    
    def __str__(self):
        return super().__str__ (f'{self.__name} {self.__age} {self.__hobby}')
