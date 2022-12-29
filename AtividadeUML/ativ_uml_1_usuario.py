from ativ_uml_1_postagem import Postagem


class Usuario:

    postagens: Postagem = []

    def __init__(self,id, nome, login, senha) -> None:
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
