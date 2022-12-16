
class Cliente: #classe Cliente onde serão carregados os dados dos clientes
    def __init__(self, nome, sobrenome, cpf): #construtor de Cliente com parâmetros públicos
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def __str__(self): #str que retorna o nome do cliente.
        return self.nome