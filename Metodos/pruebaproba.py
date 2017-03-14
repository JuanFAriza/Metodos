import numpy as np
import random

familias = np.array([])
hombres = 0
mujeres = 0

for i in range(1000):
    familia = np.array([])
    while True:
        a = random.random()
        if a <= 0.51:
            familia = np.append(familia,0)
        else:
            familia = np.append(familia,1)
            break
    familias = np.append(familias,familia)
print familias
for i in familias:
    for j in familias[i]:
        if familias[i][j] == 0:
            hombres += 1
        else:
            mujeres += 1

print hombres
print mujeres
