
n = int(input())

agenda = {}

for i in range (n):
    entrada = input()
    nome = entrada.split()[0]
    numero = int(entrada.split()[1])
		
    agenda[nome] = numero 

consulta = input() # first consulta

while (True):
    if consulta in agenda:
        saida = consulta.strip()+"="+str(agenda[consulta])
        print(saida)
    else:
        print("Not found")
   
    try:
         consulta = input()
    except:
        break