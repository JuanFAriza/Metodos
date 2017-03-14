import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def generarAleatorioenLaEsfera(N):
    phi = 2*np.pi*np.random.random(N)
    cosTheta = 2*np.random.random(N) - 1
    theta = np.arccos(cosTheta)
    return theta,phi

theta, phi = generarAleatorioenLaEsfera(100000)
x = np.sin(theta)*np.cos(phi)
y = np.sin(theta)*np.sin(phi)
z = np.cos(theta)

ax.scatter(x,y,z)
plt.show()
