import numpy as np
import matplotlib.pyplot as plt

def u0(x,L):
    return np.sin(2*np.pi*x/L)

def du_dt0(x):
    return 0

def ResolverOnda(u_0,du_dt_0,c=0.5,L=float(10),T=float(10),delta_x=0.1,delta_t=0.05):
    x = np.linspace(0,L,int((L/delta_x)+1))
    uj = u_0(x,L)
    r2 = (c*delta_t/delta_x)**2
    for j in range(int(T/delta_t)):
        if (j==0):
            uj_1 = np.copy(uj)
            uj = uj_1 + (r2/2)*(np.roll(uj_1,-1)-2*uj_1+np.roll(uj_1,1))
            uj[0]=0
            uj[-1]=0
        else:
            uj1 = 2*uj-uj_1+np.roll(r2*uj,1)-2*r2*uj+np.roll(r2*uj,-1)
            uj_1 = uj.copy()
            uj = uj1.copy()
            uj[0]=0
            uj[-1]=0
    return x,uj

def Graficar():
    a,b = ResolverOnda(u0,du_dt0,T=0)
    plt.plot(a,b,label='T = 0')
    a,b = ResolverOnda(u0,du_dt0,T=18)
    plt.plot(a,b,label='T = 10')
    plt.show()

Graficar()
