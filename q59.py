import numpy as np
arr=np.array([1,3,5,6,7,8,9,4,12])
arr1=arr.reshape(3,3)
arr2=arr1.reshape(-1)
print(arr1)
print(arr2)