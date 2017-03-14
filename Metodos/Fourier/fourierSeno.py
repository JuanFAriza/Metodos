import numpy as np
import matplotlib.pyplot as plt

def Fourier(N):
    x = np.linspace(0,2*np.pi*(1-1/(N)),N)
    f_puntos = np.sin(x)

    fgorro_puntos = np.zeros(N,dtype=complex)

    for k in range(N):
        for n in range(N):
            fgorro_puntos[k] += f_puntos[n]*np.cos(2*np.pi*k*n/N) -1j*f_puntos[n]*np.sin(2*np.pi*k*n/N)

    print np.fft.fft(f_puntos)
    print fgorro_puntos

    plt.plot(np.real(np.fft.fft(f_puntos)), label="img")
    plt.plot(np.imag(np.fft.fft(f_puntos)))
    plt.plot(f_puntos)
    plt.axes()
    plt.show()

    return fgorro_puntos

N = 20
Fourier(N)
