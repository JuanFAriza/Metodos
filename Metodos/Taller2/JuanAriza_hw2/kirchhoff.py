import numpy as np
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


def generarSistema(datos):
	n = int(datos[0][0])
	R1 = float(datos[1][0])
	R2 = float(datos[2][0])
	V1 = float(datos[3][0])
	V2 = float(datos[4][0])
	R = [R1,R2]
	V = [V1,V2]
	mat = np.zeros([n,n],dtype=float)
	vect = np.zeros(n,dtype=float)
	for i in range(n):
		mat[i,i] = 2*R[i%2]+R[(i+1)%2]
		if (i+1 < n):
			mat[i,i+1] = -R[(i+1)%2]
		if (i > 0):
			mat[i,i-1] = -R[i%2]
		vect[i] = V[i%2] - V[(i+1)%2]
	return mat, vect

def eliminacionGaussiana(matA,vectB):
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

def Resolver(datos):
	A, b = generarSistema(datos)
	sol = eliminacionGaussiana(A,b)
	fileout = open("corrientes.dat", "w")
	for i in range(len(sol)):
		fileout.write("%f\n" %(sol[i]))
	fileout.close()

Resolver(datos)
