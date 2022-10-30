class BombaCombustivel():

    def __init__(self, tipo_combustivel, valor_litro, qtd_combustivel):
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__qtd_combustivel = qtd_combustivel

    def get_tipo_combustivel(self):
        return self.__tipo_combustivel

    def get_valor_litro(self):
        return self.__valor_litro

    def get_qtd_combustivel(self):
        return self.__qtd_combustivel

posto = []
bomba = []
combustivel = {}
test = 1

print ('Cadastro inicial')
while test != 0:
    combustivel['tipo'] = (input('Digite o tipo de combustível: '))
    combustivel['valor'] = float(input('Digite o valor por litro de combustível: '))
    combustivel['qtd'] = float(input('Digite a quantidade total do tanque para este combutível: '))
    
    bomba.append(combustivel.copy())

    test = (int(input('Digite 0 para sair')))

# for combustivel in bomba:
    for v in combustivel.values():
        posto[v] = BombaCombustivel(bomba['tipo'],bomba['valor'],bomba['qtd'])
        # print(f'o Campo {k} tem valor {v}')
# print(combustivel)

# for combustivel in bomba:
#     for v in combustivel.values():
#         print (v, end=' ')
#     print()

for instancias in posto:
    print (posto[instancias].get_tipo_combustivel(), posto[instancias].get_valor_litro(), posto[instancias].get_qtd_combustivel())

# bomba1 = BombaCombustivel(bomba['tipo'],bomba['valor'],bomba['qtd'])

# print (bomba1.get_tipo_combustivel(), bomba1.get_valor_litro(), bomba1.get_qtd_combustivel())

# print (bomba.values())
# print (bomba.keys())
# print (bomba.items())