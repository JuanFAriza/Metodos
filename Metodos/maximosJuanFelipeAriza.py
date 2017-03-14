import numpy as np

def R(theta,v_0):
    return np.float(2*v_0*v_0*np.sin(theta)*np.cos(theta)/9.8)

def derivada(theta,v_0):
    delta = np.float(theta)/10000
    return (R(theta+(delta/2.0),v_0)-R(theta-(delta/2.0),v_0))/delta

def segunda_derivada(theta,v_0):
    delta = np.float(theta)/10000
    return (derivada(theta+(delta/2.0),v_0)-derivada(theta-(delta/2.0),v_0))/delta

def maximo(theta_ini):
    v = 3 #velocidad inicial
    confianza = 10**-4
    theta_max = theta_ini*np.pi/180
    while (abs(derivada(theta_max,v)) > confianza):
        theta_max -= derivada(theta_max,v)/(100*segunda_derivada(theta_max,v))
    return 180*(theta_max%(2*np.pi))/np.pi

def imprimir():
    inicial = np.linspace(0.0001,89.9,7)
    lista = np.array([ [inicial[0],maximo(inicial[0])],[inicial[1],maximo(inicial[1])],[inicial[2],maximo(inicial[2])],[inicial[3],maximo(inicial[3])],[inicial[4],maximo(inicial[4])],[inicial[5],maximo(inicial[5])],[inicial[6],maximo(inicial[6])] ])

    print lista

imprimir()
