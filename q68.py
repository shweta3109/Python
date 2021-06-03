from numpy import random
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr_s=random.shuffle(arr1)
print(arr_s)
print(arr1)

arr2=np.array([5,6,7,8,9])
arr_p=random.permutation(arr2)
print(arr_p)
print(arr2)