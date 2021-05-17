from matplotlib import pyplot as plt
from matplotlib import style
from numpy import genfromtxt
data = genfromtxt('/home/shashikantv/Documents/VSCode/Python/accl.csv',delimiter=',')
plt.plot(data)
plt.title('Accl data')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.show()