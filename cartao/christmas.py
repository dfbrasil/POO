from mensagem import CartaoMensagem


class MensagemNatal(CartaoMensagem):

    def __init__(self, nome, remetente):
        super().__init__(nome)
        self.rementente = remetente


    def __str__(self):
        return (f'{self.get_nome()}, Oh oh oh ! Feliz Natal!! Ass:  {self.rementente}')