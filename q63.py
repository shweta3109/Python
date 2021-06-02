import numpy as np
arr=np.array([1,4,5,6])
x=np.searchsorted(arr,[2,5.5],side='right')
print(x)
