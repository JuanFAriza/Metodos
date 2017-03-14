#include <stdio.h>
#include <stdlib.h>

int main(void){
  int i;
  int j;
  double p;
  double res;
  int N1 = 0; // Numero de veces que Bob tiene 3 y Alice 5
  int N2 = 0; // De los casos 1 numero de veces que los ultimos 3 son de Bob
  int pruebas = 8; // Numero de veces que se lanza
  int repeticiones;
  int *resultados; // 1 para Alice, 0 para Bob
  int suma = 0;
  double random;

  srand48(1);

  resultados = malloc(pruebas*sizeof(int));
  for (i=0;i<repeticiones;i++){
    p = drand48();
    suma = 0;
    for (j=0;j<pruebas;j++){
      res = drand48();
      if (res>p){
	resultados[j] = 1;
	suma = suma + 1;
      }
      if (res<=p){
	resultados[j] = 0;
      }
    }
    if (suma == 5){
      N1 = N1 + 1;
      if (resultados[pruebas-1] == 0){
	if (resultados[pruebas-2] == 0){
	  if (resultados[pruebas-3] == 0){
	    N2 = N2 +1;
	  }
	}
      }
    }
  }
  printf("%d / %d",N2,N1);
  return(1);
}
