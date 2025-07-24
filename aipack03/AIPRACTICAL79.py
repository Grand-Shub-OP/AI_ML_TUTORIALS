import numpy as np
import matplotlib.pyplot as plt
#plotting with default settings
x=np.linspace(-np.pi, np.pi, 3 , endpoint=True)
print("X=",x)

S=np.sin(x)
C=np.cos(x)

plt.plot(x,S,label='sin curve')
plt.plot(x,C,label='cos curve')
plt.grid(True)
plt.legend(loc="upper left")
plt.show()