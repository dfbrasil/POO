
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr, float)
    b = True
    m = []
    for i in a:
        if i is(float):
            b = True
        else:
            b = False

    if b is True:        

        for i in reversed(a):
            j = int(i)
            l = str(j)
            m.append(l+'.')
            k = numpy.array(m, float)
    
        return k
    
    else:

        for i in reversed(a):            
            m.append(i)
            k = numpy.array(m, float)

        return k


arr = input().strip().split(' ')
result = arrays(arr)
print(result)