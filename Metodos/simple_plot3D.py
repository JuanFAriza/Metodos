import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

n_points  = 100
x = np.random.random(n_points)
y = np.random.random(n_points)
z = np.random.random(n_points)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

o=fig.gca(projection='3d')
o.scatter(x,y,z)


o.set_xlabel('x')
o.set_ylabel('y')
o.set_zlabel('z')

plt.savefig('3dplot.pdf')
plt.show() 
