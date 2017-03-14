import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import os

file = open(sys.argv[1], 'rt')
try:
    lector = csv.reader(file)
    datos = []
    for linea in lector:
        datos.append(linea)

finally:
    file.close()

def y_tt(yt,k,m):
    return (-k/m)*(2*yt-np.roll(yt,1)-np.roll(yt,-1))

def Solucion(data):
    N = int(data[0][0]) #Numero de osciladores
    T = float(data[1][0]) #Tension de la cuerda
    m = float(data[2][0]) #Masa de cada oscilador
    a = float(data[3][0]) #Separacion entre osciladores
    y_ini = data[4][0].split() #Posicion inicial de cada oscilador
    for i in range(len(y_ini)):
        y_ini[i] = float(y_ini[i])
    y_vel_ini = data[5][0].split() #Velocidad inicial de cada oscilador
    for i in range(len(y_vel_ini)):
        y_vel_ini[i] = float(y_vel_ini[i])
    
    k = T/a #Constante de resorte
    Nt = 100 # Total de muestras sacadas en el tiempo
    tiempo = 2*N*a*np.sqrt(m/(a*T)) #Periodo del primer modo normal
    t = np.linspace(0,tiempo,Nt) #Array de los tiempos que se buscan
    Nx = N+2 #Agrega los dos extremos fijos
    y_ini = np.array(y_ini)
    y_ini = np.append(0,y_ini)
    y_ini = np.append(y_ini,0)
    y_vel_ini = np.array(y_vel_ini)
    y_vel_ini = np.append(0,y_vel_ini)
    y_vel_ini = np.append(y_vel_ini,0)

    ynt,ynt_t = Resolver(y_tt,Nx,t,y_ini,y_vel_ini,k,m,delta_t=tiempo/(10*N*Nt))

    x = np.array(range(Nx))
    Graficar(x,ynt,ynt_t,t,k,m)

def Resolver(y_tt,Nx,t,yn_0,yn_t0,k,m,delta_t):
    ynt = np.zeros([len(t),Nx],dtype=float)
    ynt_t = np.zeros([len(t),Nx],dtype=float)
    y = yn_0
    y_t = yn_t0
    ynt[0] = y.copy()
    ynt_t[0] = y_t.copy()
    i = 1
    for j in range(1,int((t[-1]/delta_t))+1):
        y_tmedio = y_t + 0.5*delta_t*y_tt(y,k,m)
        y_tmedio[0] = 0
        y_tmedio[-1] = 0
        y = y + delta_t*y_tmedio
        y_t = y_tmedio + 0.5*delta_t*y_tt(y,k,m)
        y_t[0] = 0
        y_t[-1] = 0
        if (abs(j*delta_t - t[i]) <= delta_t/2):
            ynt[i] = y.copy()
            ynt_t[i] = y_t.copy()
            i = i+1
        if i == len(t) + 1:
            j = int((t[-1]/delta_t))+2
    return ynt,ynt_t

def Graficar(x,ynt,ynt_t,t,k,m):
    E0 = 0.5*m*((ynt_t[0])**2)+0.5*k*(((ynt[0]-np.roll(ynt,1))**2)+((ynt[0]-np.roll(ynt[0],-1))**2))
    A = np.sqrt((np.max(E0)*2/k))
    GraficarMovimiento(x,ynt,t,A)
    GraficarEnergia(ynt,ynt_t,t,k,m)

def GraficarMovimiento(x,ynt,t,A):
    if (os.path.exists("figs_jfariza10_temp")):
        command = 'rm figs_jfariza10_temp -r'
        os.system(command)
    command = 'mkdir figs_jfariza10_temp'
    os.system(command)
    os.chdir('figs_jfariza10_temp')
    
    decimales = int(-np.log10(t[-1]/len(t)))+1
    filenames = ''

    for i in range(len(ynt)):
        y = ynt[i].copy()
        fig = plt.figure()
        ax = plt.axes()
        ax.set_xlabel("Oscilador")
        ax.set_ylabel("Desplazamiento")
        ax.set_title(format(len(x)-2) + " Osciladores Acoplados")

        plt.plot(x,y,label="Tiempo " + format(round(t[i],decimales)) + " s")
        plt.ylim(-A,A)
        ax.legend()

        filename = 'fig_temp_' + format(i) + '.png'
        plt.savefig(filename,format='png')
        plt.close()

        filenames = filenames + ' ' + filename
    
    command = 'convert -delay 10 -loop 0 ' + filenames + ' movimiento.gif'
    os.system(command)
    command = 'mv movimiento.gif ..'
    os.system(command)
    os.chdir('..')
    command = 'rm figs_jfariza10_temp -r'
    os.system(command)

def GraficarEnergia(ynt,ynt_t,t,k,m):
    E = np.zeros(len(t),dtype=float)
    E_rel = np.zeros(len(t),dtype=float)
    for i in range(len(t)):
        v = ynt_t[i]
        x1 = ynt[i] - np.roll(ynt[i],1)
        x2 = ynt[i] - np.roll(ynt[i],-1)
        E[i] = 0.5*m*np.sum(v**2) + 0.5*k*(np.sum(x1**2 + x2**2))
        E_rel[i] = (E[i] - E[0])/E[0]
    fig = plt.figure()
    ax = plt.axes()
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("(E(t)-E(0))/E(0)")
    ax.set_title("Variacion de energia en el tiempo")

    plt.plot(t,E_rel)
    ax.legend()
    
    filename = 'energia.pdf'
    plt.savefig(filename,format='pdf',transparent=True)
    plt.close()

Solucion(datos)
