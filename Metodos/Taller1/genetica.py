import numpy as np

class Expresion:
    def __init__(self, kr=1, kp=60, gammar=0.2, gammap=(1.0/30), r0=0, p0=0, deltaT=0.0003, Tfinal=150):
        self.kr = kr
        self.kp = kp
        self.gammar = gammar
        self.gammap = gammap
        self.r0 = r0
        self.deltaT = deltaT
        self.Tfinal = Tfinal
        pasos = (Tfinal+0.0)/deltaT

    def resuelve(self):
