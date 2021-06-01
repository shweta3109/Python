import numpy as np
arr=np.array([1,6,7,9,10])
x=arr.copy()
y=arr.view()
print(x)
print(y)
arr[0]=567
print(x)
print(y)
print(x.base)
print(y.base)