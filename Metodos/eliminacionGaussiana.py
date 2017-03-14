import numpy as np

a = np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]], dtype=np.float)
b = np.array([-4,3,9,7])
x = np.linalg.solve(a,b)

def eliminacionGaussiana(mat,vect):
    matA = np.array(mat)
    vectB = np.array(vect)
    matA = np.float_(matA)
    vectB = np.float_(vectB)
    if len(matA) == len(vectB):
        for j in range(len(matA)):
            var = matA[j,j]
            matA[j] = (1.0/var)*matA[j]
            vectB[j] = (1.0/var)*vectB[j]
            for i in range(len(matA)):
                if i != j:
                    var = matA[i,j]
                    matA[i] = -var*matA[j]+matA[i]
                    vectB[i] = -var*vectB[j]+vectB[i]
        return vectB

sol = eliminacionGaussiana(a,b)
print sol
x = np.linalg.solve(a,b)
print x
y = np.matmul(a,sol)-b
print y
print a
print b
