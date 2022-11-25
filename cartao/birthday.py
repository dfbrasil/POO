from mensagem import CartaoMensagem


class MensagemAniversario(CartaoMensagem):

    def __init__(self, nome,  remetente):
        super().__init__(nome)
        self.rementente = remetente

    def __str__(self):
        return (f'Parabéns {self.get_nome()}, muitos anos de vida! {self.rementente} ')
