import numpy as np
import matplotlib.pyplot as plt

M = 100000
datos = []

archivo = open('scores_A.dat','rt')
lineas = archivo.readlines()
archivo.close()

for i in lineas:
    linea = i.split('\n')
    datos.append(float(linea[0]))

archivo = open('scores_B.dat','rt')
lineas = archivo.readlines()
archivo.close()

for i in lineas:
    linea = i.split('\n')
    try:
        datos.append(float(linea[0]))
    except ValueError:
        break

aleatorios = np.array(datos)

y = []
for i in range(M):
    np.random.shuffle(aleatorios)
    diferencia = (aleatorios[:8]).mean() - (aleatorios[8:]).mean()
    y.append(diferencia)

plt.hist(y,bins=50)
plt.show()
