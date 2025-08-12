import matplotlib.pyplot as plt
from matplotlib import pyplot
import pandas

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=names)

dataframe.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)

plt.show()