#example-7
#----------------

import matplotlib.pyplot as plt
import numpy as np

#evenly sampled time at 200ms intervals
t=np.arange(0.0, 5.0, 0.2)
print(t)

#red stars , blue squares , green dots
plt.plot( t, t, 'r*-',
                t,t+3, 'bs-',
                t,t+6, 'go-',
                t,t+9, 'ro',
                t,t+9, 'k-',
                markersize=7)

plt.show()