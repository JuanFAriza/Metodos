import random

class Poblacion:
    def __init__(self, probabilidad_hombre=0.5, num_parejas=1):
        self.cantidad_hombres = 0
        self.cantidad_mujeres = 0
        self.prob_hombre = probabilidad_hombre
        self.num_parejas = num_parejas
        self.error = False

    def procrear(self):
        if self.num_parejas < 1:
                self.error = True
        elif self.num_parejas%1 != 0.0:
            self.error = True
        elif self.prob_hombre >= 1:
            self.error = True
        else:
            for i in range(self.num_parejas):
                while True:
                    r = random.random()
                    if r <= self.prob_hombre:
                        self.cantidad_hombres += 1
                    else:
                        self.cantidad_mujeres +=1
                        break

    def censar(self):
        if self.error:
            print "Error en la probabilidad de hombres o cantidad de parejas"
        else:
            print "Hay ", self.cantidad_hombres, " hijos"
            print "Hay ", self.cantidad_mujeres, " hijas"
            print "El porcentaje de hijos es ", (100.0*self.cantidad_hombres/(self.cantidad_hombres+self.cantidad_mujeres)), " %"
            print "El porcentaje de hijas es ", (100.0*self.cantidad_mujeres/(self.cantidad_hombres+self.cantidad_mujeres)), " %"
