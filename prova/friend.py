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

    def play(self, lista_amigos):

        if len(lista_amigos) == 0:
            return (f'jogar {self.__hobby}')
        
        elif len(lista_amigos) == 1:
            return (f'jogar {self.__hobby} com {lista_amigos[0]}')
        
        elif len(lista_amigos) == 2:
            return (f'jogar {self.__hobby} com {lista_amigos[0]} e {lista_amigos[1]}')

        else:
            texto = f'jogando {self.__hobby} com '
            texto_complementar = ''
            cont = 0
            for amigo in lista_amigos:
                if cont == len(lista_amigos) - 1:
                    texto_complementar += f'e {amigo}'
                else:
                    texto_complementar += f'{amigo}, '
                    cont += 1
            return texto + texto_complementar
    
    def __str__(self):
        return super().__str__ (f'{self.__name} {self.__age} {self.__hobby}')

    
    """
        Implementação do método __eq__
    """
    def __eq__(self, other):
        if self.get_name() == other.get_name() and self.get_age() == other.get_age() and self.get_hobby() == other.get_hobby():
            return True
        else:
            return False