
class Cadeira():
    modelo = 'DX Series'
    fabricante = "DX"
    peso = 30
    carga = 180
    preco = 2000
    inicio_grau = 0

    def __init__(self, preco, fabricante):
        self.preco = preco
        self.fabricante = fabricante

    def girar(self, grau_giro):
        self.inicio_grau += grau_giro
        self.inicio_grau = self.inicio_grau % 360
        return 


cadeira_1 = Cadeira(4000, 'Teste')

print (cadeira_1.preco)
print (cadeira_1.fabricante)

"""
cadeira_2 = Cadeira()

cadeira_2.preco = 3000

print (cadeira_2.preco)

print(cadeira_1.inicio_grau)
cadeira_1.girar()

print(cadeira_1.inicio_grau)
"""
