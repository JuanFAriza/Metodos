lineas.dat : cuenta.py salida.txt # Multiples requerimientos de una regla se separan con espacio
	python cuenta.py

salida.txt : a.out # Al escribir primero esta linea revisa si aparece el de la derecha en el makefile y que se haya actualizado
	./a.out > salida.txt 

a.out : hola.c # Si el archivo de la izquierda es mas viejo que el de la derecha ejecuta lo de la siguiente linea
	gcc hola.c # Se separa por un tab el comando que se quiere ejecutar
#	./a.out # Puedo introducir varios comandos despues de una regla, tambien puedo introducir un make como comando, eg. make salida.txt

clean: # Este target no tiene requirement entonces no se ejecuta, solo cuando se escribe make clean
	rm -f a.out salida.txt lineas.dat
