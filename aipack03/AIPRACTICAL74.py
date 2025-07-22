import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,2,3,4,5],'bo-',label='team 1',linewidth=2)

plt.plot([1,2,3,4,5],[1,2,3,4,5],'rs-', label='team 2', linewisth=10)

plt.axis([0,6,8,26])

plt.legend(loc="upper left")

plt.show()