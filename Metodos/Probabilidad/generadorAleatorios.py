import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

N = 10**4

m = 134456
n = 8121
k = 28411

def generar(idum):
    idum = (idum*n + k)%m
    ran = idum/float(m)
    return idum, ran

aleatorios = np.array([],dtype=float)

idum = 1
for i in range(N):
    idum, ran = generar(idum)
    aleatorios = np.append(aleatorios,ran)

#plt.hist(aleatorios)
#plt.show()

def generarGauss(idum):
    idum,ran = generar(idum)
    ranGauss = norm.ppf(ran)
    return idum, ranGauss

aleatorios = np.array([],dtype=float)

idum = 1
for i in range(N):
    idum, ran = generarGauss(idum)
    aleatorios = np.append(aleatorios,ran)

plt.hist(aleatorios,bins=30)
plt.show()

def generarGaussCirculo():
    phi = 2*np.pi*np.random.rand()
    gamma = -np.log(np.random.rand())
    
    r = sigma*np.sqrt(2*gamma)
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    return x,y
