import random
import numpy as np
import matplotlib.pyplot as plt

class Walk:
    def __init__(self, n_points=10000, step=1.0, pos_init=0):
        self.n_points = n_points
        self.pos = range(n_points)
        self.time = range(n_points)
        self.step = step
        self.pos[0] = pos_init

    def run(self):
        for i in range(1,self.n_points):
            r = random.random()
            if(r<=0.5):
                step = self.step;
            else:
                step = -self.step

            self.pos[i] = self.pos[i-1] + step
            self.time[i] = self.time[i-1] + self.step

    def writetxt(self, filename='walk.txt'):
        f = open(filename, 'w')
        for i in range(self.n_points):
            f.write('{} {}\n'.format(self.time[i], self.pos[i]))
        f.close()

    def quiebra(self):
        for i in range(self.n_points):
            if self.pos[i] == 0:
                print "quiebra en ",i," pasos"
                break
            if i == self.n_points-1:
                print "no quebro"
                break

class Apostador:
    def __init__(self, pos_init=0):
        self.time = 0
        self.time_pierde = 0
        self.pos = pos_init

    def run(self):
        while True:
            r = random.random()
            self.time += 1
            if(r<=0.5):
                self.pos += 1
            else:
                self.pos -= 1
            if self.pos == 0:
                self.time_pierde = self.time
                break

class Apuestas:
    def __init__(self, dinero_inicial=10, cantidad_apostadores=10):
        self.d_ini = dinero_inicial
        self.c_apostadores = cantidad_apostadores
        self.t_perdidas = np.array([])

    def apostar(self):
        self.t_perdidas = np.array([])
        for i in range(self.c_apostadores):
            p=Apostador(pos_init=self.d_ini)
            p.run()
            self.t_perdidas = np.append(self.t_perdidas, p.time_pierde)


    def imprimir(self):
        fig = plt.figure()
        bins = np.linspace(0, 3000, 100)
        plt.hist(self.t_perdidas, bins)
        filename = 'histperdidas'
        plt.savefig(filename + '.pdf', format = 'pdf', transparent = True)
        plt.show()
        plt.close()
