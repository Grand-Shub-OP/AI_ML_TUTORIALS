#example 3
#------------------
#g- = green solid line
#ro = red circle dot

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[1,4,9,16],'ro-')
plt.xlabel("----some numbers---->")
plt.ylabel("----Squared Values------->")

plt.axis([0,5,0,17])

plt.show()
