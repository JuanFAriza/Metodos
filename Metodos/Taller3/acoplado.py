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

def y_tt(yt,k):
    return (-k)*(2*yt-np.roll(yt,1)-np.roll(yt,-1))

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
    
    k = T/(m*a) #Constante de "resorte"
    Nt = 20 #Total de muestras en el tiempo, que se sacan
    tiempo = 2*N*a*np.sqrt(m/(a*T)) #Tiempo que dura la simulacion, el periodo del primer modo normal
    t = np.linspace(0,tiempo,Nt) #Array de los tiempos que se buscan
    Nx = N+2
    y_ini = np.array(y_ini)
    y_ini = np.append(0,y_ini)
    y_ini = np.append(y_ini,0)
    y_vel_ini = np.array(y_vel_ini)
    y_vel_ini = np.append(0,y_vel_ini)
    y_vel_ini = np.append(y_vel_ini,0)
    ynt,ynt_t = Resolver(y_tt,Nx,t,y_ini,y_vel_ini,k,delta_t=tiempo/(10000.0*Nt))
    x = np.array(range(Nx))
    
    Graficar(x,ynt,ynt_t,m,k,t)

def Resolver(y_tt,Nx,t,yn_0,ynt_0,k,delta_t=0.00000005):
    ynt = np.zeros([len(t),Nx])
    ynt_t = np.zeros([len(t),Nx])
    y_t_ = ynt_0
    y_ = yn_0
    ynt[0] = y_.copy()
    ynt_t[0] = y_t_.copy()
    i = 1
    y = y_ #Introducido para DKD
    y_t = y_t_ #Introducido para DKD
    for j in range(1,int(t[-1]/delta_t)+1):
        y_tmedio = y_t + 0.5*delta_t*y_tt(y,k)
        y_tmedio[0] = 0
        y_tmedio[-1] = 0
        y = y + delta_t*y_tmedio
        y_t = y_tmedio + 0.5*delta_t*y_tt(y,k)
        """
        y_t_medio = y_t + 0.5*delta_t*y_tt(y,k)
        y = y + delta_t*y_t_medio
        y_t = y_t_medio + 0.5*delta_t*y_tt(y,k)
        y_t[0] = 0
        y_t[-1] = 0
        y[0] = 0
        y[-1] = 0
        """
        """
        y_medio = y + 0.5*delta_t*y_t
        y_medio[0] = 0
        y_medio[-1] = 0
        y_t = y_t + delta_t*y_tt(y_medio,k)
        y_t[0] = 0
        y_t[-1] = 0
        y = y_medio + 0.5*delta_t*y_t
        """
        
        """
        if j==1:
            y = y_ + delta_t*y_t_
            y_t = y_t_ + delta_t*y_tt(y_,k)
            y[0] = 0
            y[-1] = 0
            y_t[0] = 0
            y_t[-1] = 0
        else:
            y_t1  = y_t_ + 2*delta_t*y_tt(y,k)
            y1 = y_ + 2*delta_t*y_t
            y_t_ = y_t
            y_t = y_t1
            y_t[0] = 0
            y_t[-1] = 0
            y_ = y
            y = y1
            y[0] = 0
            y[-1] = 0
        """
        if (abs(j*delta_t - t[i]) <= delta_t/2):
            ynt[i] = y.copy()
            ynt_t[i] = y_tmedio.copy()
            i += 1
            print t[i-1]
            print ynt[i-1]
            print ynt_t[i-1]
    return ynt,ynt_t

def Graficar(x,ynt,ynt_t,m,k,t):
    E0 = 0.5*m*ynt_t[0]*ynt_t[0] + 0.5*k*ynt[0]*ynt[0]
    A = 2*np.sqrt((2.0/k)*np.max(E0))
    GraficarMovimiento(x,ynt,A,t)
    GraficarEnergia(ynt,ynt_t,m,k,t)

def GraficarMovimiento(x,ynt,A,t):
    if (os.path.exists("figs_jfariza10_temp")):
        command = 'rm figs_jfariza10_temp -r'
        os.system(command)
    command = 'mkdir figs_jfariza10_temp'
    os.system(command)
    os.chdir('figs_jfariza10_temp')
    
    decimales = int(-np.log10(t[-1]/len(t)))+1
    filenames = ''
    for i in range(len(ynt)):
        y = ynt[i]
        fig = plt.figure()
        ax = plt.axes()
        ax.set_xlabel("Oscilador")
        ax.set_ylabel("y")
        ax.set_title("{} Osciladores Acoplados".format(len(x)-2))
        
        plt.plot(x,y, label="Tiempo {} s".format(round(t[i],decimales)))
        plt.ylim(-A,A)
        ax.legend()
        
        filename = 'fig_temp_{}.png'.format(i)
        plt.savefig(filename, format='png')
        plt.close()
        
        filenames = filenames + ' ' + filename
    command = 'convert -delay 10 -loop 0 ' + filenames + ' movimiento.gif'
    os.system(command)
    command = 'mv movimiento.gif ..'
    os.system(command)
    os.chdir('..')
    command = 'rm figs_jfariza10_temp -r'
    os.system(command)

def GraficarEnergia(ynt,ynt_t,m,k,t):
    E = t.copy()
    E_rel = E.copy()
    for i in range(len(t)):
        x = ynt[i]
        v = ynt_t[i]
        x2 = x*x
        v2 = v*v
        E[i] = 0.5*m*np.sum(v2) + 0.5*k*np.sum(x2)
        E_rel[i] = (E[i]-E[0])/E[0]
    fig = plt.figure()
    ax = plt.axes()
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("(E(t)-E(0))/E(0)")
    ax.set_title("Variacion de energia vs. tiempo")
    
    plt.plot(t,E_rel)
    ax.legend()
    
    filename = 'energia.pdf'
    plt.savefig(filename, format='pdf', transparent=True)
    plt.close()

Solucion(datos)
