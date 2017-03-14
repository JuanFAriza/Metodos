import numpy as np
import matplotlib.pyplot as plt

N = 10**6 # Numero de pasos
x0 = 1 # Origen
delta = 0.1 # El paso va a tener una longitud en [-delta,delta]
sigma = 1

x = np.array([x0],dtype='float')

def q(x1,x2): # Probabilidad de pasar a x1 dado que estoy en x2
    return 1 # Vamos a asumir que hay la misma probabilidad de saltar a la derecha o a la izquierda

def p(x): # Probabilidad de estar en la posicion x
    return (1/(np.sqrt(2*np.pi)*sigma))*np.exp(-x**2/(2*sigma**2))

def U(): # Un numero aleatorio que va a decidir si se da el salto o no
    return np.random.rand()

for i in range(N-2):
    xnew = x[i] + (np.random.rand() - 0.5)*2*delta # Posible posicion nueva
    alpha = min(1,(p(xnew)/p(x[i]))*(q(xnew,x[i])/q(x[i],xnew)))
    u = U()
    if (u < alpha):
        x = np.append(x,xnew)
    else:
        x = np.append(x,x[i])

plt.hist(x,bins=50)
plt.show()
