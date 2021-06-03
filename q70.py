from numpy import  random
from matplotlib import pyplot
import seaborn as sns
sns.kdeplot(random.chisquare(df=1,size=1000))
pyplot.show()