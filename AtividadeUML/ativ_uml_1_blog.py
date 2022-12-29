import datetime

from ativ_uml_1_postagem import Postagem


class Blog:

    postagens: Postagem = []

    def __init__(self) -> None:
       pass 
        
    def adicionar_postagem(self,postagem):
        self.postagens.append(postagem)

    def publicar_postagem(self, postagem):
        print (postagem)

    def listar_postagens_publicadas(self):
        for post in Blog.postagens:
            if (datetime.datetime.now() > post.dataPublicacao):
                print(post)

    def listar_todas_as_postagem(self):
        for post in self.postagens:
            print(post.text)

    def apagar_postagem(self, postagem:Postagem):
        for post in self.postagens:
            if (post == postagem):
                self.postagens.remove(post)

