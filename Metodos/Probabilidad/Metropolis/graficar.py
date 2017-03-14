import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('datos.dat')
x = data[:,0]

plt.hist(x)
plt.show()
