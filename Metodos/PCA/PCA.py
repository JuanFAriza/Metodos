import numpy as np
import matplotlib.pyplot as plt

"""
data_A = np.loadtxt('data_A.txt')
x = data_A[:,0]
y = data_A[:,1]

cov_matA = np.zeros((2,2))
cov_matA[0,0] = np.mean((x - x.mean())*(x - x.mean()))
cov_matA[0,1] = np.mean((y - y.mean())*(x - x.mean()))
cov_matA[1,0] = np.mean((y - y.mean())*(x - x.mean()))
cov_matA[1,1] = np.mean((y - y.mean())*(y - y.mean()))

print cov_matA
"""

data_B = np.loadtxt('data_B.txt')
x = data_B[:,0]
y = data_B[:,1]

cov_matB = np.zeros((2,2))
cov_matB[0,0] = np.mean((x - x.mean())*(x - x.mean()))
cov_matB[0,1] = np.mean((y - y.mean())*(x - x.mean()))
cov_matB[1,0] = np.mean((y - y.mean())*(x - x.mean()))
cov_matB[1,1] = np.mean((y - y.mean())*(y - y.mean()))

values, vectors = np.linalg.eig(np.cov(x,y))
eigen_vect_can = vectors.T

cambio_base_t = np.linalg.inv(vectors).T
data_cambio = np.matmul(data_B,cambio_base_t)

eigen_vect = np.matmul(eigen_vect_can,cambio_base_t)

val_x = 10
set_x = np.array([-val_x,val_x])
set_y1 = (eigen_vect[0][1]/eigen_vect[0][0])*set_x
set_y2 = (eigen_vect[1][1]/eigen_vect[1][0])*set_x

set_1 = np.array([-val_x*eigen_vect[0],val_x*eigen_vect[0]])
set_2 = np.array([-val_x*eigen_vect[1],val_x*eigen_vect[1]])

print cov_matB
print np.cov(x,y)
print np.linalg.eig(np.cov(x,y))

fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Subespacios propios")

#plt.plot(set_1[:,0],set_1[:,1], label="subespacio 1")
#plt.plot(set_2[:,0],set_2[:,1], label="subespacio 2")

plt.plot(set_1[:,0],set_1[:,1], label="subespacio 1")
plt.plot(set_2[:,0],set_2[:,1], label="subespacio 2")
plt.scatter(data_cambio[:,0],data_cambio[:,1], label="distribucion")
ax.legend()
plt.show()


"""
data_C = np.loadtxt('data_C.txt')
x = data_C[:,0]
y = data_C[:,1]
z = data_C[:,2]

cov_matC = np.zeros((3,3))
cov_matC[0,0] = np.mean((x - x.mean())*(x - x.mean()))
cov_matC[0,1] = np.mean((y - y.mean())*(x - x.mean()))
cov_matC[1,0] = np.mean((y - y.mean())*(x - x.mean()))
cov_matC[1,1] = np.mean((y - y.mean())*(y - y.mean()))
cov_matC[0,2] = np.mean((x - x.mean())*(z - z.mean()))
cov_matC[2,0] = np.mean((z - z.mean())*(x - x.mean()))
cov_matC[1,2] = np.mean((y - y.mean())*(z - z.mean()))
cov_matC[2,1] = np.mean((z - z.mean())*(y - y.mean()))
cov_matC[2,2] = np.mean((z - z.mean())*(z - z.mean()))

print cov_matC
"""
