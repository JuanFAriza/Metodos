import numpy as np
import matplotlib.pyplot as plt

def der_x(x,y,z,rho,sigma,beta):
    return sigma*(y-x)

def der_y(x,y,z,rho,sigma,beta):
    return x*(rho-z)-y

def der_z(x,y,z,rho,sigma,beta):
    return x*y-beta*z

def RungeKutta(x_0=float(2),y_0=float(3),z_0=float(4),delta_t=0.01,t_final=float(40),rho=float(28),sigma=float(10),beta=8.0/3.0):
    N = int((t_final/delta_t)+1)
    x = np.zeros(N)
    y = np.zeros(N)
    z = np.zeros(N)
    x[0] = x_0
    y[0] = y_0
    z[0] = z_0
    for i in range(1,N):
        x_media = x[i-1] + (delta_t/2)*der_x(x[i-1],y[i-1],z[i-1],rho,sigma,beta)
        y_media = y[i-1] + (delta_t/2)*der_y(x[i-1],y[i-1],z[i-1],rho,sigma,beta)
        z_media = z[i-1] + (delta_t/2)*der_z(x[i-1],y[i-1],z[i-1],rho,sigma,beta)
        x[i] = x[i-1] + delta_t*der_x(x_media,y_media,z_media,rho,sigma,beta)
        y[i] = y[i-1] + delta_t*der_y(x_media,y_media,z_media,rho,sigma,beta)
        z[i] = z[i-1] + delta_t*der_z(x_media,y_media,z_media,rho,sigma,beta)
    return x,y,z

def Graficar():
    x,y,z = RungeKutta()
    nom = ['X vs. Y','X vs. Z','Y vs. Z']
    label = [['X','Y'],['x','Z'],['Y','Z']]
    sets = [[x,y],[x,z],[y,z]]
    for i in range(3):
        fig = plt.figure()
        ax = plt.axes()
        ax.set_xlabel(label[i][0])
        ax.set_ylabel(label[i][1])
        ax.set_title(nom[i])
        plt.plot(sets[i][0],sets[i][1], label = nom[i])
        ax.legend()
        plt.savefig(nom[i] + '.pdf', format = 'pdf')
        plt.close()

Graficar()       

