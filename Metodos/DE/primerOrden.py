import numpy as np
import matplotlib.pyplot as plt

def func(t):
    return np.exp(-t)

def der(y):
    return -y
"""
def Euler(f,y_0=0,t):
    euler = np.zeros(len(t))
    euler[0] = y0
    for i in range(1,len(euler)):
        euler[i] = euler[i-1]+(t[i]-t[i-1])*der(euler[i-1])
    return euler

def LeapFrog(f,y_0=0,t):
    leapfrog = np.zeros(len(t))
    leapfrog[0] = y0
    leapfrog[1] = leapfrog[0]+(t[1]-t[0])*der(leapfrog[0])
    for j in range(2,len(leapfrog)):
        leapfrog[j] = leapfrog[j-2]+(t[j]-t[j-2])*der(leapfrog[j-1])
    return leapfrog

def RungeKutta2(f,y_0=0,t):
    rungeKutta2 = np.zeros(len(t))
    rungeKutta2[0] = y0
    for k in range(1,len(rungeKutta2)):
        der_media = der(rungeKutta2[k-1]+(t[k]-t[k-1]/2)*der(rungeKutta2[k-1]))
        rungeKutta2[k] = rungeKutta2[k-1]+(t[k]-t[k-1])*der_media

def RungeKutta4(f,y_0=0,t):
    rungeKutta4 = np.zeros(N)
    rungeKutta4[0] = y0
    for l in range(1,len(rungeKutta4)):
        k1 = der(rungeKutta4[l-1])
        k2 = der(rungeKutta4[l-1]+((t[l]-t[l-1])/2)*k1)
        k3 = der(rungeKutta4[l-1]+((t[l]-t[l-1])/2)*k2)
        k4 = der(rungeKutta4[l-1]+(t[l]-t[l-1])*k3)
        k = (1/6.0)*(k1+2*k2+2*k3+k4)
        rungeKutta4[l] = rungeKutta4[l-1]+(t[l]-t[l-1])*k
"""

def graficar(N):
    y0 = 1
    delta = 5/float(N-1)
    euler = np.linspace(0,5,N)
    leapfrog = np.zeros(N)
    rungeKutta2 = np.zeros(N)
    rungeKutta4 = np.zeros(N)
    t = np.linspace(0,5,N)
    euler[0] = y0
    leapfrog[0] = y0
    rungeKutta2[0] = y0
    rungeKutta4[0] = y0
    an = func(t)

    for i in range(1,len(euler)):
        euler[i] = euler[i-1]+delta*der(euler[i-1])
    leapfrog[1] = leapfrog[0]+delta*der(leapfrog[0])
    for j in range(2,len(leapfrog)):
        leapfrog[j] = leapfrog[j-2]+2*delta*der(leapfrog[j-1])
    for k in range(1,len(rungeKutta2)):
        der_media = der(rungeKutta2[k-1]+(delta/2)*der(rungeKutta2[k-1]))
        rungeKutta2[k] = rungeKutta2[k-1]+delta*der_media
    for l in range(1,len(rungeKutta4)):
        k1 = der(rungeKutta4[l-1])
        k2 = der(rungeKutta4[l-1]+(delta/2)*k1)
        k3 = der(rungeKutta4[l-1]+(delta/2)*k2)
        k4 = der(rungeKutta4[l-1]+delta*k3)
        k = (1/6.0)*(k1+2*k2+2*k3+k4)
        rungeKutta4[l] = rungeKutta4[l-1]+delta*k
    plt.plot(t,an)
    plt.plot(t,euler)
    plt.plot(t,leapfrog)
#    plt.plot(t,abs(an-euler))
#    plt.plot(t,abs(an-leapfrog))
#    plt.plot(t,abs(an-rungeKutta2))
#    plt.plot(t,abs(an-rungeKutta4))
    plt.show()

graficar(1000000)
