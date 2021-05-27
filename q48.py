import matplotlib.pyplot as plt
import numpy as np
font1={'family':'Times New Roman','color':'red','size':'14'}
x=np.array([0,1,2,3])
y=np.array([0,1,2,3])
plt.xlabel("Number of hours",fontdict=font1)
plt.ylabel("Wage",fontdict=font1)
plt.title("Data",loc='center')

plt.plot(x,y)

plt.show()
exit()