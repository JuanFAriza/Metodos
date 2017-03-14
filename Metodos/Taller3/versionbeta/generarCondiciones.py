import numpy as np
import sys
import os

N = int(sys.argv[1])
T = float(sys.argv[2])
m = float(sys.argv[3])
a = float(sys.argv[4])

print N

def seno(y):
    y_ = np.linspace(0,np.pi,(len(y)+2))
    y_ = np.delete(np.delete(y_,0),-1)
    return np.sin(y_)

y = np.zeros(N)
print y
y_ = seno(y)
print y_

if os.path.exists("condiciones.dat"):
    command = "rm condiciones.dat"
    os.system(command)

fileout = open("condiciones.dat", "w")

fileout.write("%i\n"%(N))
fileout.write("%f\n"%(T))
fileout.write("%f\n"%(m))
fileout.write("%f\n"%(a))
for i in y_:
    fileout.write("%f "%(i))
fileout.write("\n")
for i in y:
    fileout.write("%f "%(i))
fileout.close()
