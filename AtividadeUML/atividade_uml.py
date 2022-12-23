
class Date:

    def __init__(self):
         pass

class Contrato:

    def __init__(self, salario):
         self.__inicio = Date()
         self.__fim = Date()
         self.__salario = salario

class Pessoa:

    def __init__(self, nome, sexo):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nasc = Date()


class Aluno(Pessoa):

    def __init__(self, nome, sexo, matric):
        super().__init__(nome, sexo)
        self.__matric = matric

class Ator(Pessoa):
    
    def __init__(self, nome, sexo):
        super().__init__(nome, sexo)
        self.__contrato = Contrato()


class Personagem(Ator):

        def __init__(self, nome, sexo, contrato, caracterizacao, novela):
            super().__init__(nome, sexo, contrato)
            self.__caracterizacao = caracterizacao
            self.__novela = novela

