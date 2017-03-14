import numpy as np
import sys
import csv
import datetime
import time

#file = open(sys.argv[1], 'rt')

file = open("AirQualityUCI.csv", 'rt') #Borrar, es solo para correr desde interprete
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
    del a[-1]
    del a[-1]
    medidas.append(a)

del medidas[0]

eliminar = np.array([],dtype='int')
for i in range(len(medidas)): #Encuentra entradas vacias, donde no se tomo ningun dato
    if (medidas[i][0] == ''):
        eliminar = np.append(eliminar,i)
for i in range(len(eliminar)):
    del medidas[eliminar[i]]
    eliminar -= 1

medidas = np.array(medidas)
fechas = np.reshape(medidas[:,[0]].copy(),len(medidas[:,[0]]))

horas = np.reshape(medidas[:,[1]].copy(),len(medidas[:,[1]]))


hora0 = time.mktime(datetime.datetime(int(fechas[0].split('/')[2]),int(fechas[0].split('/')[1]),int(fechas[0].split('/')[0]),int(horas[0].split('.')[0])).timetuple())/3600 #Hora desde la cual se empezo a medir

t = np.array([],dtype='float') #Arreglo de horas medidas desde la hora0
for i in range(len(fechas)):
    hora = time.mktime(datetime.datetime(int(fechas[i].split('/')[2]),int(fechas[i].split('/')[1]),int(fechas[i].split('/')[0]),int(horas[i].split('.')[0])).timetuple())/3600
    t = np.append(t,hora-hora0)

CO = np.array(medidas[:,[2]].copy(),dtype='float')
CO = np.reshape(CO,len(CO))
CO = CO - CO.mean() #Centrarlo en la media, para solo medir variaciones
CO = np.array([t.copy(),CO]).T

NMHC = np.array(medidas[:,[4]].copy(),dtype='float')
NMHC = np.reshape(NMHC,len(NMHC))
NMHC = NMHC - NMHC.mean() #Centrarlo en la media, para solo medir variaciones
NMHC = np.array([t.copy(),NMHC]).T

C6H6 = np.array(medidas[:,[5]].copy(),dtype='float')
C6H6 = np.reshape(C6H6,len(C6H6))
C6H6 = C6H6 - C6H6.mean() #Centrarlo en la media, para solo medir variaciones
C6H6 = np.array([t.copy(),C6H6]).T

NOx = np.array(medidas[:,[7]].copy(),dtype='float')
NOx = np.reshape(NOx,len(NOx))
NOx = NOx - NOx.mean() #Centrarlo en la media, para solo medir variaciones
NOx = np.array([t.copy(),NOx]).T

NO2 = np.array(medidas[:,[9]].copy(),dtype='float')
NO2 = np.reshape(NO2,len(NO2))
NO2 = NO2 - NO2.mean() #Centrarlo en la media, para solo medir variaciones
NO2 = np.array([t.copy(),NO2]).T

concentraciones = [CO,NMHC,C6H6,NOx,NO2]

for i in range(len(concentraciones)): #Elimina las entradas faltantes (-200)
    eliminar = np.array([],dtype='int')
    for j in range(len(concentraciones[i])):
        if concentraciones[i][j][1]==-200:
            eliminar = np.append(eliminar,j)
    for j in range(len(eliminar)):
        concentraciones[i] = np.reshape(np.delete(concentraciones[i],[2*eliminar[j],2*eliminar[j]+1]),[len(concentraciones[i])-1,2])
        eliminar -= 1

transformadas = []
for i in range(len(concentraciones)):
    transformadas.append(np.zeros(int(concentraciones[i][-1][0]+1),dtype='complex'))
for i in range(len(transformadas)):
    for m in range(len(transformadas[i])):
        Pm = 0+0j
        for n in range(len(concentraciones[i])):
            Pm += concentraciones[i][n][1]*np.exp(-1j*m*2*np.pi*concentraciones[i][n][0]/(concentraciones[i][-1][0]+1))
        transformadas[i][m] = Pm
        print i,m

indicesMax = []
for i in range(len(transformadas)): #Busco los componentes mas fuertes, teniendo en cuenta que la amplitud de ciertas (las que no son N/2) frecuencias w, se dividen en dos en w y -w
    indicesMax.append([0,1])
    for j in range(int(len(transformadas[i])/2)):
        if (j%(int((len(transformadas[i])+1)/2)) == 0) and (indicesMax[i][0]%(int((len(transformadas[i])+1)/2)) == 0):
            if abs(transformadas[i][indicesMax[i][0]]) < abs(transformadas[i][j]):
                indicesMax[i][0] = j
        if (j%(int((len(transformadas[i])+1)/2)) != 0) and (indicesMax[i][0]%(int((len(transformadas[i])+1)/2)) == 0):
            if abs(transformadas[i][indicesMax[i][0]]) < abs(2*transformadas[i][j]):
                indicesMax[i][0] = j
        if (j%(int((len(transformadas[i])+1)/2)) == 0) and (indicesMax[i][0]%(int((len(transformadas[i])+1)/2)) != 0):
            if abs(2*transformadas[i][indicesMax[i][0]]) < abs(transformadas[i][j]):
                indicesMax[i][0] = j
        if (j%(int((len(transformadas[i])+1)/2)) != 0) and (indicesMax[i][0]%(int((len(transformadas[i])+1)/2)) != 0):
            if abs(transformadas[i][indicesMax[i][0]]) < abs(transformadas[i][j]):
                indicesMax[i][0] = j
    for j in range(int(len(transformadas[i])/2)):
        if (j%(int((len(transformadas[i])+1)/2)) == 0) and (indicesMax[i][1]%(int((len(transformadas[i])+1)/2)) == 0):
            if abs(transformadas[i][indicesMax[i][1]]) < abs(transformadas[i][j]):
                indicesMax[i][1] = j
        if (j%(int((len(transformadas[i])+1)/2)) != 0) and (indicesMax[i][1]%(int((len(transformadas[i])+1)/2)) == 0):
            if abs(transformadas[i][indicesMax[i][1]]) < abs(2*transformadas[i][j]):
                indicesMax[i][1] = j
        if (j%(int((len(transformadas[i])+1)/2)) == 0) and (indicesMax[i][1]%(int((len(transformadas[i])+1)/2)) != 0):
            if abs(2*transformadas[i][indicesMax[i][1]]) < abs(transformadas[i][j]):
                indicesMax[i][1] = j
        if (j%(int((len(transformadas[i])+1)/2)) != 0) and (indicesMax[i][1]%(int((len(transformadas[i])+1)/2)) != 0):
            if abs(transformadas[i][indicesMax[i][1]]) < abs(transformadas[i][j]):
                indicesMax[i][1] = j

fileout = open("periodos.dat", "w")
for i in range(len(transformadas)):
    frecuencias = [24*indicesMax[i][0]/(concentraciones[i][-1][0]+1),24*indicesMax[i][1]/(concentraciones[i][-1][0]+1)]
    fileout.write("%f %f\n"%(frecuencias[0],frecuencias[1]))
fileout.close()
