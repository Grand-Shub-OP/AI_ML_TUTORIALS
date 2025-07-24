import numpy as np
import matplotlib.pyplot as plt
#plotting with default settings
x=np.linspace(-np.pi, np.pi, num 255, endpoint=true)
print("X=",X)

S=np.sin(X)
C=np.cos(x)

plt.plot(X,S,label='sin curve')
plt.plot(X,c,label='cos curve')
plt.grid(true)
plt/legend(loc+"upper left")
plt.show()