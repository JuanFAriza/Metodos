import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq


def complexExp(value):
    re, im = np.cos(value), np.sin(value)       # since the use of complex numbers was limited
    return np.array([re, im])
    
def gaussiana(x):
    return np.exp(-(x*x)/0.02)

def fourierCoeff(points):
    N = len(points)
    a_n = np.zeros(N)
    b_n = np.zeros(N)
    
    for k in range(N):
        suma = 0
        for n in range(N):
            suma += points[n]*complexExp(-2.0*float(n)*np.pi*k/N)
        a_n[k], b_n[k] = suma    
    return a_n, b_n
    
N = 20
delta_t = 2.0*np.pi/(N)
x = np.linspace(0,2.0*np.pi - delta_t, N)
y = np.sin(x) #+ 0.20*np.sin(20.0*x)+ 0.40*np.sin(40.0*x)
a_n, b_n = fft(y)

print(a_n, b_n)

"""
plt.plot(x,y)
plt.savefig('time.pdf')
plt.clf()

plt.plot(np.arange(N), a_n)
plt.savefig('freq_real.pdf')
plt.clf()

plt.plot(np.arange(N), b_n)
plt.savefig('freq_img.pdf')
plt.clf()


fft_x = fft(y) / n # FFT Normalized
freq = fftfreq(n, dt) # Recuperamos las frecuencias
print(freq)
plt.plot(freq,abs(fft_x))
#print(freq)
"""
