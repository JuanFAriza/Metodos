import numpy as np
import matplotlib.pyplot as plt

def bessel(m,x,theta):
    return np.cos(m*theta-x*np.sin(theta))/np.pi

def func(m,x,N=1000):
    h = np.pi/N
    i = (1/3)*h*(bessel(m,x,0)+bessel(m,x,np.pi))
    for k in range(1,N-1):
        if k%2 == 1:
            i += (4./3)*h*bessel(m,x,k*h)
        else:
            i += (2./3)*h*bessel(m,x,k*h)
    return i

def funcarray(m):
    x = np.linspace(0,20,100)
    y = func(m,x)
    return [x,y]

def graficar():
    fig = plt.figure()
    ax = plt.axes()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Bessel")
    for i in range(3):
        z = funcarray(i)
        plt.plot(z[0],z[1],label="m="+str(i))
        ax.legend()
    plt.show()
    plt.close()

graficar()
