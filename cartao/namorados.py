from cartao_mensagem import CartaoMensagem


class MensagemDiaDosNamorados(CartaoMensagem):

    def __init__(self, nome, texto, remetente):
        super().__init__(nome, texto)
        self.rementente = remetente
       

    def __str__(self):
        return (f'{self.get_nome()} namorado  {self.rementente} , {self.texto}')