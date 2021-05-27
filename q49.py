import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0,1,2,3])
y = np.array([4,5,6,7])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("expenditure")

#plot 2:
x = np.array([0,1,2,3])
y = np.array([3,4,5,6])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("savings")

plt.suptitle("comparison")
plt.show()
exit()