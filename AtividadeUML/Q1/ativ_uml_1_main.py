from ativ_uml_1_blog import Blog
from ativ_uml_1_postagem import Postagem
from ativ_uml_1_usuario import Usuario

lista_usuario = []
user1 = Usuario(1,'nome1','login1',123)
lista_usuario.append(user1)
user2 = Usuario(2,'nome2','login2',456)
lista_usuario.append(user2)
user3 = Usuario(3,'nome2','login2',789)

# for user in lista_usuario:
#     if (user1 != user):
#         exit()
#     if (user2 != user):
#         exit()
    # if (user3 != user):
    #     exit() USUARIO NAO CADASTRADO


blog = Blog()

post1 = Postagem(1,'titulo1','texto1',2022,12,29, user1,blog)
post2 = Postagem(2,'titulo2','texto2',2022,12,30, user2,blog)
post3 = Postagem(3,'titulo3','texto3',2022,12,28, user1,blog)
post4 = Postagem(4,'titulo4','texto4',2022,12,28, user3,blog)
blog.adicionar_postagem(post1)
blog.adicionar_postagem(post2)
blog.adicionar_postagem(post3)
blog.adicionar_postagem(post4)
# blog.listar_todas_as_postagem()

blog.listar_postagens_publicadas()

blog.apagar_postagem(post2)

blog.listar_todas_as_postagem()


    
