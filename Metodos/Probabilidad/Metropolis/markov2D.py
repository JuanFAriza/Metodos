import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data_trend.dat')

x = data[:,0]
y = data[:,1]

N = 10**5
delta_m = 0.001
delta_b = 0.001

m0 = 2
b0 = 8

m = np.array([m0],dtype='float')
b = np.array([b0],dtype='float')

def prob_b(b):
    if (b > 0 and b < 16):
        return 1
    else:
        return 0
def prob_m(m):
    if (m > -1 and m < 4):
        return 1
    else:
        return 0
def prob_obs_mb(x,y,m,b):
    dif = y - m*x - b
    dif2 = dif*dif
    return np.exp(-0.5*dif2.sum())

for i in range(N):
    mnew = m[i] + np.random.rand()*2*delta_m - delta_m
    bnew = b[i] + np.random.rand()*2*delta_b - delta_b
    if ((prob_obs_mb(x,y,m[i],b[i])*prob_b(b[i])*prob_m(m[i])) == 0):
        alpha = 1
    else:
        alpha = min(1,prob_obs_mb(x,y,mnew,bnew)*prob_b(bnew)*prob_m(mnew)/(prob_obs_mb(x,y,m[i],b[i])*prob_b(b[i])*prob_m(m[i])))
    u = np.random.rand()
    if (u < alpha):
        m = np.append(m,mnew)
        b = np.append(b,bnew)
    else:
        m = np.append(m,m[i])
        b = np.append(b,b[i])

plt.scatter(x,y)
x_list = np.linspace(x.min(),x.max(),100)
plt.plot(x_list,np.median(m)*x_list+np.median(b))
plt.show()
