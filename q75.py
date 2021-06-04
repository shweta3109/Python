from math import log
import numpy as np
nplog=np.frompyfunc(log,2,1)
arr=np.array([7,100])
arr1=nplog(arr,15)
print(arr1)
arr2=np.array([4,5,6])
arr3=np.log2(arr2)
print(arr3)

