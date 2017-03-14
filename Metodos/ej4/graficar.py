import matplotlib.pyplot as plt
import csv

archivo = open('datos.dat', 'rt')
ave = []
std = []
lineas = archivo.readlines()
archivo.close()

for i in range(len(lineas)):
    linea = lineas[i].split(' ')
    ave.append(float(linea[0]))
    std.append(float(linea[1]))

ax = plt.axes()
plt.scatter(ave,std)
ax.set_ylabel("desviacion")
ax.set_xlabel("promedio")
ax.legend()

plt.savefig("scatter.png",format='png')
