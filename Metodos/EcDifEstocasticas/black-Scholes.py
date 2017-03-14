import numpy as np
import matplotlib.pyplot as plt

t_ini = 0
t_fin = 1
delta_t = 0.01
N = 1000

def w(tini,tfin,deltat):
    n = int((tfin - tini)/deltat)
    t = np.linspace(tini,tfin,n+1)
    w = t.copy()
    w[0] = 0
    for i in range(1,n+1):
        w[i] = w[i-1] + np.sqrt(deltat)*np.random.normal(0,1)
    return t,w

mu = 0.75
sigma = 0.3
x0 = 307.65

def solEuler(wt,t):
    euler = t.copy()
    euler[0] = x0
    for i in range(1,len(euler)):
        euler[i] = euler[i-1]+mu*(t[i]-t[i-1])*(euler[i-1]) + sigma*(wt[i]-wt[i-1])*euler[i-1]
    return euler


t,wt = w(t_ini,t_fin,delta_t)

sol = solEuler(wt,t)

plt.plot(t,sol)
plt.show()
