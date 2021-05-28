import matplotlib.pyplot as plt
import numpy as np

y = np.array([40, 20, 15, 25])
mylabels = ["Engineers", "Doctors", "Drivers", "Cook"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Professions:")
plt.show() 