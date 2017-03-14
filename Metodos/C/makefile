Onda1D.pdf : Onda1D.dat graficar.py
	python graficar.py
	evince Onda1D.pdf &
Onda1D.dat : Onda1D.out
	./Onda1D.out > Onda1D.dat
Onda1D.out : Onda1D.c
	gcc Onda1D.c -lm -o Onda1D.out
