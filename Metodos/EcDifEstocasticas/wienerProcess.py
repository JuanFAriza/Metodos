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

t,bla = w(t_ini,t_fin,delta_t)
u = np.zeros(1 + (t_fin - t_ini)/delta_t,dtype='float')

for i in range(N):
    t,wt =  w(t_ini,t_fin,delta_t)
    uwt = np.exp(t - 0.5*wt)
    u = u + uwt/N

plt.scatter(t,u)
plt.show()
