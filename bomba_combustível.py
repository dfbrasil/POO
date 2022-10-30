
# DESAFIO VALENDO PONTO EXTRA:

# - Como poderíamos abstrair e trazer para o “metaverso” um veículo do "mundo real"? Pense nos atributos e ações de um veículo.
# - E, entāo, implemente uma classe Veiculo que o objeto possa abastecer a partir de um objeto da classe BombaCombustivel.

class BombaCombustivel():

    def __init__(self, tipo_combustivel, valor_litro, qtd_combustivel, litros_consumidos):
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__qtd_combustivel = qtd_combustivel
        self.litros_consumidos = litros_consumidos

    def get_tipo_combustivel(self):
        print(f'Tipo atual: {self.__tipo_combustivel}')
        print(' ')
        return self.__tipo_combustivel

    def get_valor_litro(self):
        print(f'Valor atual: {self.__valor_litro}')
        print(' ')
        return self.__valor_litro

    def get_qtd_combustivel(self):
        return self.__qtd_combustivel

    def abastecerPorValor(self, valor):
        litros = valor/self.__valor_litro

        if self.__qtd_combustivel < litros:
            print ('Não há combustivel disponível para a operação')
            print(' ')
            self.litros_consumidos = litros
            return self.litros_consumidos
        else:
            print (f'Foi abastecido o valor de R${valor}, o que equivale a {litros} litros de {self.__tipo_combustivel}.')
            print(' ')
            self.litros_consumidos = litros
            return self.litros_consumidos
    
    def abastecerPorLitro(self, litros): 
        valor = litros * self.__valor_litro
        if self.__qtd_combustivel < litros:
            print ('Não há combustivel disponível para a operação')
            print(' ')
            self.litros_consumidos = litros
            return self.litros_consumidos
        else:
            print(f'Foi abastecidos {litros} litros de {self.__tipo_combustivel}, o que equivale a R${valor}.')
            print(' ')
            self.litros_consumidos = litros
            return self.litros_consumidos

    def litros_consum(self):
        return self.litros_consumidos
       
    def alterarValor(self,valor):
        self.__valor_litro = valor
        print (f'O novo valor do {self.__tipo_combustivel} é de R${valor}.')
        print(' ')

    def alterarCombustivel(self,tipo):
        print (f'O novo tipo do {self.__tipo_combustivel} é de {tipo}.')
        print(' ')
        self.__tipo_combustivel = tipo
        
    def alterarQuantidadeCombustível(self):
        if self.litros_consumidos <= self.__qtd_combustivel:
            self.__qtd_combustivel -= self.litros_consumidos

        print (f'Restam {self.__qtd_combustivel} litros de {self.__tipo_combustivel}')
        print(' ')


class Veiculo(BombaCombustivel):

    def __init__(self,tipo_combustivel,tanque_atual, tanque_total, km_l, distancia):

        self.tipo_combustivel = tipo_combustivel
        self.tanque_atual = tanque_atual
        self.tanque_total = tanque_total
        self.km_l = km_l
        self.distancia = distancia
        
 
    def volume_atual(self):
        print (f'O tanque contém atualmente {self.tanque_atual} litros de {self.tipo_combustivel}')

    def autonomia(self):
        auton = self.tanque_atual * self.km_l
        print (f'Com a quantidade de combustível atual ainda se pode andar {auton} kilômentros')
    
    def viajar(self,distancia):

        qtd_necessaria_comb = (distancia / self.km_l)
        if self.tanque_atual > qtd_necessaria_comb:
            self.tanque_atual -= qtd_necessaria_comb
            print ('Boa Viagem!')
            return self.tanque_atual
        
        else:
            print ('É melhor abastecer!')
            qtd_necessaria_comb = round((distancia / self.km_l),1)
            qtd_faltante =  round((qtd_necessaria_comb - self.tanque_atual),2)
            print (f'Para realizar a viagem não nessários {qtd_necessaria_comb} litros de {self.tipo_combustivel}')
            print (f'Você precisa abastecer no mínimo {qtd_faltante} litros de {self.tipo_combustivel}')
            
    def abastecer_litros(self,litros):
        self.tanque_atual += litros
        return self.tanque_atual

    def abastecer_valor(self, valor):

        if self.tipo_combustivel == 'alcool':
            valor_comb = bomba_alcool.get_valor_litro()
            qtd_comb = round((valor/valor_comb),2)
            self.tanque_atual += qtd_comb
            return self.tanque_atual

        elif self.tipo_combustivel == 'gasolina':
            valor_comb = bomba_gasolina.get_valor_litro()
            qtd_comb = round((valor/valor_comb),2)
            self.tanque_atual += qtd_comb
            return self.tanque_atual

        elif self.tipo_combustivel == 'diesel':
            valor_comb = bomba_diesel.get_valor_litro()
            qtd_comb = round((valor/valor_comb),2)
            self.tanque_atual += qtd_comb
            return self.tanque_atual


print ('Cadastramento inicial dos componentes do posto.')
alcool_valor_litro = float(input('Digite o valor do litro de álcool: '))
alcool_qtd_tanque = float(input('Digite a quantidade inicial de litros de álcool no tanque: '))
bomba_alcool = BombaCombustivel('alcool', alcool_valor_litro, alcool_qtd_tanque, litros_consumidos=0)

print ('Cadastramento inicial dos componentes do veículo')
tipo = input('Digite o tipo de combustível do veículo: ')
tanque_atual = float(input('Digite o volume atual do tanque: '))
tanque_total = float(input('Digite o volume máximo do tanque: '))
consumo = float(input('Digite o consumo do carro em km/l: '))
carro = Veiculo(tipo, tanque_atual, tanque_total, consumo, distancia=0)

gasolina_valor_litro = float(input('Digite o valor do litro de gasolina: '))
gasolina_qtd_tanque = float(input('Digite a quantidade inicial de litros de gasolina no tanque: '))
bomba_gasolina = BombaCombustivel('gasolina', gasolina_valor_litro, gasolina_qtd_tanque, litros_consumidos=0)

diesel_valor_litro = float(input('Digite o valor do litro de diesel: '))
diesel_qtd_tanque = float(input('Digite a quantidade inicial de litros de diesel no tanque: '))
bomba_diesel = BombaCombustivel('diesel', diesel_valor_litro, diesel_qtd_tanque, litros_consumidos=0)

opcao_geral =100

while opcao_geral!= 0:
    opcao_servico = 100
    opcao_geral =100
    print ('Menu de opções gerais:')
    print('Digite "1" para BombaCombustivel: ')
    print('Digite "2" para Veículo:' )
    opcao_geral = int(input('Digite "0" para Sair: '))
    print(' ')

    if opcao_geral == 2:
        opcao_combustivel = 100
        opcao_servico = 100

        while opcao_servico != 0:
            opcao_servico = 100
            print ('Menu de opções para serviços:')
            print ('Digite "1" para verificar o volume atual do combustível: ')
            print ('Digite "2" para verificar a autonomia em km: ')
            print ('Digite "3" para viajar: ')
            print ('Digite "4" para abastecer em Reais: ')
            print ('Digite "5" para abastecer em litros: ')
            opcao_servico = int(input('Digite "0" para Sair: '))
            print(' ')

            if opcao_servico == 1:
                carro.volume_atual()
            elif opcao_servico == 2:
                carro.autonomia()
            elif opcao_servico == 3:
                distancia = float(input('Digite a distância em relação ao destino: '))
                carro.viajar(distancia)
            elif opcao_servico == 4:
                valor = float(input('Digite o valor a ser abastecido: '))
                print(' ')
                bomba_alcool.abastecerPorValor(valor)
                carro.abastecer_valor(valor)
            elif opcao_servico == 5:
                litros = float(input('Digite a quantidade de litros a ser abastecido: '))
                bomba_alcool.abastecerPorLitro(litros)
                carro.abastecer_litros(litros)
                print()

    if opcao_geral == 1:

        opcao_combustivel = 100
        opcao_servico = 100

        while opcao_combustivel != 0:
            opcao_servico = 100
            print ('Menu de opções de combustíveis:')
            print('Digite "1" para Álcool: ')
            print('Digite "2" para Gasolina:' )
            print('Digite "3" para Diesel: ')
            opcao_combustivel = int(input('Digite "0" para Sair: '))
            print(' ')

            if opcao_combustivel == 1:
                while opcao_servico != 0:
                    print ('Menu de opções para serviços:')
                    print ('Digite "1" para verificar o tipo atual do combustível: ')
                    print ('Digite "2" para verificar o valor atual por litro de combustível: ')
                    print ('Digite "3" para verificar a quantidade restante no tanque: ')
                    print ('Digite "4" para abastecer em Reais: ')
                    print ('Digite "5" para abastecer em litros: ')
                    print ('Digite "6" para alterar o valor por litro de combustível: ')
                    print ('Digite "7" para alterar o tipo do combustível: ')
                    opcao_servico = int(input('Digite "0" para Sair: '))
                    print(' ')

                    if opcao_servico == 1:
                        bomba_alcool.get_tipo_combustivel()
                    elif opcao_servico == 2:
                        bomba_alcool.get_valor_litro()
                    elif opcao_servico == 3:
                        bomba_alcool.alterarQuantidadeCombustível()
                    elif opcao_servico == 4:
                        valor = float(input('Digite o valor a ser abastecido: '))
                        print(' ')
                        bomba_alcool.abastecerPorValor(valor)
                    elif opcao_servico == 5:
                        litros = float(input('Digite a quantidade de litros a ser abastecido: '))
                        bomba_alcool.abastecerPorLitro(litros)
                        print()
                    elif opcao_servico == 6:
                        valor = float(input('Digite o novo valor por litro do combustível: '))
                        bomba_alcool.alterarValor(valor)
                    elif opcao_servico == 7:
                        tipo = input('Digite o novo tipo do combustível: ')
                        print(' ')
                        bomba_alcool.alterarCombustivel(tipo)

            if opcao_combustivel == 2:
                while opcao_servico != 0:
                    print ('Menu de opções para serviços:')
                    print ('Digite "1" para verificar o tipo atual do combustível: ')
                    print ('Digite "2" para verificar o valor atual por litro de combustível: ')
                    print ('Digite "3" para verificar a quantidade restante no tanque: ')
                    print ('Digite "4" para abastecer em Reais: ')
                    print ('Digite "5" para abastecer em litros: ')
                    print ('Digite "6" para alterar o valor por litro de combustível: ')
                    print ('Digite "7" para alterar o tipo do combustível: ')
                    opcao_servico = int(input('Digite "0" para Sair: '))
                    print(' ')

                    if opcao_servico == 1:
                        bomba_gasolina.get_tipo_combustivel()
                    elif opcao_servico == 2:
                        bomba_gasolina.get_valor_litro()
                    elif opcao_servico == 3:
                        bomba_gasolina.alterarQuantidadeCombustível()
                    elif opcao_servico == 4:
                        valor = float(input('Digite o valor a ser abastecido: '))
                        print(' ')
                        bomba_gasolina.abastecerPorValor(valor)
                    elif opcao_servico == 5:
                        litros = float(input('Digite a quantidade de litros a ser abastecido: '))
                        bomba_gasolina.abastecerPorLitro(litros)
                        print()
                    elif opcao_servico == 6:
                        valor = float(input('Digite o novo valor por litro do combustível: '))
                        bomba_gasolina.alterarValor(valor)
                    elif opcao_servico == 7:
                        tipo = input('Digite o novo tipo do combustível: ')
                        print(' ')
                        bomba_gasolina.alterarCombustivel(tipo)

            if opcao_combustivel == 3:
                while opcao_servico != 0:
                    print ('Menu de opções para serviços:')
                    print ('Digite "1" para verificar o tipo atual do combustível: ')
                    print ('Digite "2" para verificar o valor atual por litro de combustível: ')
                    print ('Digite "3" para verificar a quantidade restante no tanque: ')
                    print ('Digite "4" para abastecer em Reais: ')
                    print ('Digite "5" para abastecer em litros: ')
                    print ('Digite "6" para alterar o valor por litro de combustível: ')
                    print ('Digite "7" para alterar o tipo do combustível: ')
                    opcao_servico = int(input('Digite "0" para Sair: '))
                    print(' ')

                    if opcao_servico == 1:
                        bomba_diesel.get_tipo_combustivel()
                    elif opcao_servico == 2:
                        bomba_diesel.get_valor_litro()
                    elif opcao_servico == 3:
                        bomba_diesel.alterarQuantidadeCombustível()
                    elif opcao_servico == 4:
                        valor = float(input('Digite o valor a ser abastecido: '))
                        print(' ')
                        bomba_diesel.abastecerPorValor(valor)
                    elif opcao_servico == 5:
                        litros = float(input('Digite a quantidade de litros a ser abastecido: '))
                        bomba_diesel.abastecerPorLitro(litros)
                        print()
                    elif opcao_servico == 6:
                        valor = float(input('Digite o novo valor por litro do combustível: '))
                        bomba_diesel.alterarValor(valor)
                    elif opcao_servico == 7:
                        tipo = input('Digite o novo tipo do combustível: ')
                        print(' ')
                        bomba_diesel.alterarCombustivel(tipo)