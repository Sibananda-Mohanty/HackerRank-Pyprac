import numpy as np

x = np.array(input().split(),dtype=int)
y =  np.array(input().split(),dtype=int)
print(np.inner(x,y))
print(np.outer(x,y))