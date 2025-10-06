import numpy as np
from numpy import random 

arr = random.randint(1,100,size = 50)
arr[0] = 50
print(arr)
target = 50
arr.sort()
print(arr)

start = 0 
end = len(arr)- 1 
while start <= end : 
    mid = (start + end) // 2
    if target > arr[mid]:
        start = mid + 1
    elif target < arr[mid]:
        end = mid - 1 
    else :
        print(mid)
        print(arr[mid ])
        break                

print("as u can see it doesnt exist")