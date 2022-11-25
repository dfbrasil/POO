from cartao_mensagem import CartaoMensagem


class MensagemAniversario(CartaoMensagem):

    def __init__(self, nome, texto, remetente):
        super().__init__(nome, texto)
        self.rementente = remetente

    def __str__(self):
        return (f'Parabéns {self.get_nome()} {self.rementente} , {self.texto}')
