
class CartaoMensagem:


    def __init__(self, nome, texto):
        self.__nome = nome
        self.texto = texto

    def get_nome(self):
        return self.__nome

