import matplotlib.pyplot as plt
import numpy as np
import csv

file = open('Onda1D.dat','rt')
try:
    lector = csv.reader(file)
    datos = []
    for linea in lector:
        datos.append(linea)

finally:
    file.close()

print datos[0]

y = np.array([],dtype='float')
for i in range(len(datos)):
    y = np.append(y,float(datos[0][0]))

filename = 'Onda1D.pdf'
plt.plot(y)
plt.savefig(filename,format='pdf',transparent=True)

plt.close
