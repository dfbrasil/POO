import datetime


class Postagem:

    def __init__(self,id,titulo,text,ano,mes,dia,usuario,blog) -> None:
        self.id = id
        self.titulo = titulo
        self.text = text
        self.dataPublicacao = datetime.datetime(ano,mes,dia)
        self.usuario = usuario
        self.blog = blog

    def __str__(self) -> str:
        return (f'ID: {self.id}, TITULO: {self.titulo}, TEXT: {self.text}, DATA: {self.dataPublicacao}')
