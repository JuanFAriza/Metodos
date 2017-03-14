import numpy as np
import matplotlib.pyplot as plt
import sys
import csv

file = open(sys.argv[1], 'rt')

try:
    lector = csv.reader(file)
    datos = []
    for linea in lector:
        datos.append(linea)
    
finally:
    file.close()

medidas = []
for dato in datos:
    medida = dato[0]
    for j in range(1,len(dato)):
        medida += '.' + dato[j]
    a = medida.split(';')
    del a[-1] #Borra ultimas dos columnas que no contienen informacion
    del a[-1]
    medidas.append(a)

del medidas[0] #Elimina el encabezado

eliminar = np.array([],dtype='int')
for i in range(len(medidas)): #Encuentra los indices vacios o con un dato deseado incompleto
    if (medidas[i][0]=='') or (medidas[i][2]=='-200') or (medidas[i][4]=='-200') or (medidas[i][5]=='-200') or (medidas[i][7]=='-200') or (medidas[i][9]=='-200'):
        eliminar = np.append(eliminar,i)
for i in range(len(eliminar)): #Elimina las tomas con datos deseados incompletos
    del medidas[eliminar[i]]
    eliminar -= 1

medidas = np.array(medidas)
medidas = medidas[:,[2,4,5,7,9]]
medidas = np.array(medidas,dtype='float')

CO = medidas[:,[0]].copy()
CO = np.reshape(CO,len(CO))
NMHC = medidas[:,[1]].copy()
NMHC = np.reshape(NMHC,len(NMHC))
C6H6 = medidas[:,[2]].copy()
C6H6 = np.reshape(C6H6,len(C6H6))
NOx = medidas[:,[3]].copy()
NOx = np.reshape(NOx,len(NOx))
NO2 = medidas[:,[4]].copy()
NO2 = np.reshape(NO2,len(NO2))

mediciones = np.array([CO,NMHC,C6H6,NOx,NO2]) #Mediciones originales
mediciones_promedio = np.mean(mediciones,1)
mediciones_estandar = np.add(mediciones.T,-mediciones_promedio).T #A cada dato le resto su promedio
varianza_mediciones_estandar = np.sqrt(np.mean((mediciones_estandar)**2,1))
mediciones_estandar = np.divide(mediciones_estandar.T,varianza_mediciones_estandar).T #Cada muestra se divide por su varianza

mat_cov = np.zeros([len(mediciones_estandar),len(mediciones_estandar)],dtype='float')
for i in range(len(mat_cov)):
    for j in range(len(mat_cov)):
        mat_cov[i][j] = np.mean((mediciones_estandar[i] - mediciones_estandar[i].mean())*(mediciones_estandar[j] - mediciones_estandar[j].mean()))

values, vectors_estandar = np.linalg.eig(mat_cov)

indicesPCA = [0,1]

for i in range(len(values)):
    if values[i] > values[indicesPCA[0]]:
        indicesPCA[0] = i
for i in range(len(values)):
    if i != indicesPCA[0]:
        if values[i] > values[indicesPCA[1]]:
            indicesPCA[1] = i

vectors = np.multiply(vectors_estandar.T,varianza_mediciones_estandar).T #Vuelvo a reescalar multiplicando por las varianzas
norma_vectors = np.sqrt(np.sum((vectors**2),0))
vectors = np.divide(vectors,norma_vectors) #Normalizo los vectores de PCA reescalados

cambioBase = np.linalg.inv(vectors) #Tomo la inversa del cambio de base PCA a canonica
mat_cambio = np.matmul(cambioBase,mediciones) #Multiplico el cambio de base por las medidas
comp1 = mat_cambio[indicesPCA[0]] #Componente principal
comp2 = mat_cambio[indicesPCA[1]] #Componente secundario

fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("{}".format(vectors.T[indicesPCA[0]]))
ax.set_ylabel("{}".format(vectors.T[indicesPCA[1]]))
plt.scatter(comp1,comp2)
ax.legend()
plt.savefig("pca.pdf", format='pdf', transparent=True)
plt.close()

fileout = open("pca.dat", "w")
for i in range(len(comp1)):
    fileout.write("%f %f\n" %(comp1[i],comp2[i]))
fileout.close()

porcentaje = 100*(values[indicesPCA[0]]+values[indicesPCA[1]])/np.sum(values)
fileout = open("varianza.dat", "w")
fileout.write("%f"%(porcentaje))
fileout.close()
