import numpy as np 

def add(x,y):
    return x+y


add = np.frompyfunc(add,2,1)

print(add([1,2,3,4,5],[1,2,3,4,5]))
print(np.add([1,2,3,4,5],[1,2,3,4,5]))