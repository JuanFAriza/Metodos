scatter.png : datos.dat graficar.py
	python graficar.py

datos.dat : aleatorio.out
	./aleatorio.out > datos.dat

aleatorio.out : generador.c
	gcc generador.c -lm -o aleatorio.out
clean:
	rm scatter.png -r
