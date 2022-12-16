from elevador import Elevador

opcao = 1

capacidade = int(input('Capacidade do elevador: '))
andares = int(input('Número de andares do prédio: '))
andar_atual = 0


elevador = Elevador(capacidade, andares, 0, 0)

while(opcao != 0):
    print ('Digite sua opção')
    print ('1 - para entrar')
    print ('2 - para sair')
    print ('3 - para subir')
    print ('4 - para descer')
    print ('5 - Qual o andar atual? ')
    print ('6 - Quantas pessoas tem no elevador? ')
    opcao = int(input('0 - para fechar o programa: '))

    if opcao == 1:
        elevador.entrar(capacidade)
    elif opcao == 2:
        elevador.sair(capacidade)
    elif opcao == 3:
        elevador.subir(andar_atual)
    elif opcao == 4:
        elevador.descer(andar_atual)
    elif opcao == 5:
        elevador.get_andar_atual()
    elif opcao == 6:
        elevador.get_num_pessoas()