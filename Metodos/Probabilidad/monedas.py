import numpy as np

M = 100000 # Numero de muestras
exitosos = 0
N = 30 # numero de lanzamientos

for i in range(M):
    muestra = np.random.random(N)
    muestra[muestra<0.5] = 0
    muestra[muestra>=0.5] = 1
    caras = 0
    for j in muestra:
        if j == 0:
            caras += 1
    if caras >= 22:
        exitosos += 1

print (exitosos+0.0)/(M+0.0)
