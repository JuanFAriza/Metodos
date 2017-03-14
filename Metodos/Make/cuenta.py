f = open('salida.txt')
l = f.readlines()
f.close()

n = len(l)

f = open('lineas.dat', 'w')
f.write('{}\n'.format(n))
f.close()
