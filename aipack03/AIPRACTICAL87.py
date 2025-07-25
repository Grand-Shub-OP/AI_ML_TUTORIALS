import matplotlib.pyplot as plt
mylabels = ['S1', 'S2', 'S3']
sections = [ 60, 90, 50]
myColors = ['c', 'g', 'r']

plt.pie(sections, labels=mylabels, colors=myColors,
        startangle = 0,
        explode    = (0,0,0.1),
        autopct    = '%.2f %%'  )

plt.title('Pie Chart Example')
plt.show()