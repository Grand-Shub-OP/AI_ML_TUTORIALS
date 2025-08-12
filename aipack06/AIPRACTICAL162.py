import pandas as pd

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=names)

dataframe.plot(kind='density', subplots=True, layout=(3,3), sharex=False)

plt.tight_layout()
plt.show()