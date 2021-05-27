import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apple", "Banana", "Cherry", "grapes"])
y = np.array([7, 8, 6, 10])

plt.barh(x, y, height = 0.4)
plt.show()
exit()