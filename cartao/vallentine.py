from mensagem import CartaoMensagem


class MensagemDiaDosNamorados(CartaoMensagem):

    def __init__(self, nome, remetente):
        super().__init__(nome)
        self.rementente = remetente
       

    def __str__(self):
        return (f'{self.get_nome()} você é a luz do meu túnel! Ass:  {self.rementente}')