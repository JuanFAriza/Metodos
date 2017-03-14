import numpy as np
import matplotlib.pyplot as plt

def u_0(x):
    return np.exp(-(x-2)**2)

def Resolver(u0_x,t,c=0.5,L=10,delta_x=0.1,delta_t=0.05,T=200):
    x = np.linspace(0,L,(L/delta_x)+1)
    uj = u0_x(x)
    j_ = int(t/delta_t)
    for j in range(j_):
        uj = uj - c*delta_t*(uj-np.roll(uj,1))/delta_x
    return x,uj

def Lax_Wendroff(u0_x,t,c=0.5,L=100,delta_x=0.1,delta_t=0.05,T=200):
    x = np.linspace(0,L,(L/delta_x)+1)
    uj = u0_x(x)
    j_ = int(t/delta_t)
    alpha = c*delta_t/delta_x
    b_1 = alpha*(alpha+1)/2
    b0 = 1-alpha**2
    b1 = alpha*(alpha-1)/2
    for j in range(j_):
        uj = b_1*np.roll(uj,1)+b0*uj+b1*np.roll(uj,-1)
    return x,uj

def Graficar():
    a,b = Resolver(u_0,0)
    plt.plot(a,b)
    a,b = Resolver(u_0,80)
    plt.plot(a,b,label='Upwind')
    a,b = Lax_Wendroff(u_0,80)
    plt.plot(a,b,label='Lax-Wendroff')
    plt.show()

Graficar()
