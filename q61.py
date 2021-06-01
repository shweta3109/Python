import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([6,7,8,9])
arr=np.concatenate((arr1,arr2),axis=0)
print(arr)
arr3=np.stack((arr1,arr2),axis=1)
print(arr3)