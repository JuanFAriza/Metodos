import numpy as np

h = float(6.62606957E-34) # En kilogramo metro cuadrado por segundo
c = float(299792458) # En metros por segundo
k = float(1.38064852E-23) # En kilogramo metro cuadrado por segundo cuadrado por Kelvin


def I_aux(y,T): # devuelve (ch)^2/2k^3 I(ky/h,T), dI_aux(y,T) = cte * dI(ky/h,T) = 0, v = ky/h, dI(v,T) = 0
	return (y**3)/(np.exp(y/T)-1)

def dI_aux(y,T):
	dy = float(1E-5)
	return (I_aux(y+dy,T)-I_aux(y-dy,T))/(2*dy)

def max_I_aux(T):
	a = float(1)
	b = float(1)
	while (dI_aux(a,T) < 0):
		a = a/2
	while (dI_aux(b,T) > 0):
		b = b*2
	epsilon = float(1E-7) # Intervalo de confianza
	while (abs(dI_aux(a+(b-a)/2,T)) > epsilon):
		if (dI_aux(a+(b-a)/2,T) >= 0):
			a = a+(b-a)/2
		if (dI_aux(a+(b-a)/2,T) < 0):
			b = a+(b-a)/2
	c = k/h # Factor para pasar de y a v
	return c*(a+(b-a)/2) # Esta en Hz/K

def Wien(N):
	T = np.random.random(N)*np.logspace(1,8,N)
	b_array = np.zeros(N)
	for i in range(N):
		b_ = max_I_aux(T[i])/T[i]
		b_array[i] = b_
	b = float(np.mean(b_array)*(10**-9)) # Toma el promedio y lo pasa a GHz/K
	fileout = open("b.dat", "w")
	fileout.write("%f" %(b))
	fileout.close()

Wien(20)