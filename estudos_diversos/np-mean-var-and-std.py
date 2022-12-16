import numpy

x,y = input().split()
lista = []

for i in range(int(x)):
    arr = numpy.array(list(map(int,input().split())))
    lista.append(arr)

print(numpy.mean(lista,axis =1 ))
print(numpy.var(lista,axis = 0))
print(round(numpy.std(lista),11))
