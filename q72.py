import numpy as np
def mymul(x,y):
  return x*y
mymul=np.frompyfunc(mymul,2,1)
print(mymul([1,2,3],[6,8,9]))