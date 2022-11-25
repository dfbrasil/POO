from cartao_mensagem import CartaoMensagem


class MensagemNatal(CartaoMensagem):

    def __init__(self, nome, texto, remetente):
        super().__init__(nome, texto)
        self.rementente = remetente


    def __str__(self):
        return (f'{self.get_nome()}, Oh oh oh ! Feliz Natal!! Ass:  {self.rementente}, {self.texto}')