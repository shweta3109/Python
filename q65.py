import numpy as np
arr=np.array([1,4,5,7,6,4,3,2])
filter_arr=arr>3
arr1=arr[filter_arr]
print(arr1)
filter_arr2=arr%2==0
arr2=arr[filter_arr2]
print(arr2)
