
class CartaoMensagem:

    listaMsg = []

    def __init__(self, nome):
        self.nome = nome
        CartaoMensagem.listaMsg.append(MensagemAniversario)
        CartaoMensagem.listaMsg.append(MensagemDiaDosNamorados)
        CartaoMensagem.listaMsg.append(MensagemNatal)

    def __str__(self):
        for msg in (CartaoMensagem):
            print (msg)

class MensagemDiaDosNamorados(CartaoMensagem):

    def __init__(self, nome):
        mensagem = (f'Dia dos namorados {nome}')
        return mensagem 

class MensagemNatal(CartaoMensagem):

    def __init__(self, nome):
        mensagem = (f'Feliz Natal {nome}')
        return mensagem 

class MensagemAniversario(CartaoMensagem):

    def __init__(self, nome):
        mensagem = (f'Feliz Aniversario {nome}')
        return mensagem

nome = CartaoMensagem('Daniel')
