import numpy as np

Nhits = 0
N = 100000

for i in range(N):
    pos = np.random.random(2)
    pos = 2*pos - 1
    if (np.sum(pos**2) < 1):
        Nhits += 1
print 4.0*Nhits/N
