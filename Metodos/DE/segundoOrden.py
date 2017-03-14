import numpy as np
import matplotlib.pyplot as plt

def y_tt(y,t):
    return -10

def y_2tt(y,t):
    return float(-4*y)

def y_3tt(y,t):
    return -y

def EulerS_O(f, t, y_0, y_t0):
    y = np.zeros(len(t),dtype=float)
    y_t = np.zeros(len(t),dtype=float)
    delta = t[1]-t[0]
    y[0] = float(y_0)
    y_t[0] = float(y_t0)
    for i in range(1,len(y)):
        y_t[i] = y_t[i-1]+delta*f(y[i-1],t[i-1])
        y[i] = y[i-1]+delta*y_t[i-1]
    return y, y_t

def RungeKutta4S_O(f,t,y_0=0,y_t0=0):
    rungeKutta4 = np.zeros(len(t),dtype=float)
    rungeKutta4_t = np.zeros(len(t),dtype=float)
    delta = t[1]-t[0]
    rungeKutta4[0] = y_0
    rungeKutta4_t[0] = y_t0
    for l in range(1,len(rungeKutta4)):
        k1 = f(rungeKutta4[l-1],0)
        k2 = f(rungeKutta4[l-1]+(delta/2)*k1,0)
        k3 = f(rungeKutta4[l-1]+(delta/2)*k2,0)
        k4 = f(rungeKutta4[l-1]+(delta)*k3,0)
        k = (1/6.0)*(k1+2*k2+2*k3+k4)
        rungeKutta4_t[l] = rungeKutta4_t[l-1]+delta*k
        k1 = rungeKutta4_t[l-1]
        k2 = rungeKutta4_t[l-1]+(delta/2)*k
        k3 = rungeKutta4_t[l-1]+(delta/2)*k
        k4 = rungeKutta4_t[l-1]+(delta)*k
        k = (1/6.0)*(k1+2*k2+2*k3+k4)
        rungeKutta4[l] = rungeKutta4[l-1]+delta*k
    return rungeKutta4,rungeKutta4_t

def Resolver():
    t = np.linspace(0,100,10000)
    y, y_t = RungeKutta4S_O(y_3tt,t,0,10)
    plt.plot(y,y_t)
    plt.show()

Resolver()
