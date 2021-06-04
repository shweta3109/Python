import numpy as np
arr1=np.array([1,2,4,5])
arr2=np.array([5,7,8,9])
arr3=np.prod([arr1,arr2])
arr4=np.prod([arr1,arr2],axis=1)
arr5=np.cumprod([arr1,arr2])
print(arr3)
print(arr4)
print(arr5)