import numpy as np


h = float(6.62606957E-34) # En kilogramo metro cuadrado por segundo
c = float(299792458) # En metros por segundo
k = float(1.38064852E-23) # En kilogramo metro cuadrado por segundo cuadrado por Kelvin


def I_cv(x,T): # Integrando de Integral[(y**3)/(np.exp(y/T)-1)]=c^2h^3/2k^4 Integral[I] tras cambio de variables
        a = (x**3)/((np.exp(x/(T*(1-x)))-1)*((1-x)**5))

def Integral_I_cv(T,n): # La funcion I_cv integrada en [0,a(T)] es despreciable
	if (T < 10000):
		a = (1.0/2)*(float(T)/(T+1))
	if (T >= 10000):
		a = 1 - (10.0/T)*np.log(T)/np.log(10)
	b = 1
	n = int(n)
	h = (b-a)/float(n)
	integral = 0
	for i in range(n-30): # Elimina el polo en x = 1
		integral += h*I_cv(a+i*h,T)
        return np.pi*integral # Devuelve pi*Integral[I]

def Stefan(N): # N Numero de temperaturas a evaluar
	n = 1000000 # Numero de intervalos para integrar
	T = np.random.random(N)*np.logspace(1,8,N)
	cte = float(2*(k**4)/((c**2)*(h**3))) # Constante para pasar de integral de I_aux a la de I
	s = float(0)
	for i in range(N):
		s_ = cte*Integral_I_cv(T[i],n)/(T[i]**4)
		s = s + s_/float(N)
	fileout = open("s.dat", "w")
	fileout.write(str(s))
	fileout.close()

Stefan(20)
