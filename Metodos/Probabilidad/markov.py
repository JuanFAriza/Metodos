import numpy as np

Nhits = 0
pos = np.array([0.0,0.0])
delta = 0.1
N = 10**5

for i in range(N):
    var = 2*delta*np.random.random(2) - delta
    if (abs((pos + var)[0]) < 1 and abs((pos + var)[1]) < 1):
        pos = pos + var
    if (np.sum(pos**2) < 1):
        Nhits += 1
print 4.0*Nhits/N

