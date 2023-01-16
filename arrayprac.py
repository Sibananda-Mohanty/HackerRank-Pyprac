import numpy as np

def arrays(arr):
    arr = numpy.asarray(arr)
    arr = arr.astype('float')
    arr2=numpy.flip(arr)
    return(arr2)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)