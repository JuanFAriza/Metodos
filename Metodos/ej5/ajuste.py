import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('datos.dat')

x = data[:,0]
y = data[:,1]

N = 10**5
delta_a = 0.001
delta_b = 0.001
delta_c = 0.001

a0 = -5
b0 = 30
c0 = 20

a = np.array([a0],dtype='float')
b = np.array([b0],dtype='float')
c = np.array([c0],dtype='float')

def prob_obs_abc(a,b,c):
    dif = y - a*(x**2) - b*x - c
    dif2 = dif**2
    return np.exp(-0.5*dif2.sum())

for i in range(N):
    anew = a[i] + np.random.rand()*2*delta_a - delta_a
    bnew = b[i] + np.random.rand()*2*delta_b - delta_b
    cnew = c[i] + np.random.rand()*2*delta_c - delta_c
    alpha = np.exp((prob_obs_abc(anew,bnew,cnew) - prob_obs_abc(a[i],b[i],c[i])))
    alpha = min(1,alpha)

#    if ((prob_obs_abc(a[i],b[i],c[i])*prob_a(a[i])*prob_b(b[i])*prob_c(c[i])) == 0):
#        alpha = 1
#    else:
#        alpha = min(1,alpha)
    u = np.random.rand()
    if (u < alpha):
        a = np.append(a,anew)
        b = np.append(b,bnew)
        c = np.append(c,cnew)
    else:
        a = np.append(a,a[i])
        b = np.append(b,b[i])
        c = np.append(c,c[i])

a0 = np.mean(a)
b0 = np.mean(b)
c0 = np.mean(c)
print(a0,b0,c0)

plt.scatter(x,y)
x_list = np.linspace(x.min(),x.max(),100)
plt.plot(x_list,a0*x_list**2 + b0*x_list +c0)
plt.show()
