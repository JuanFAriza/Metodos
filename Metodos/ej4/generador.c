#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define m 10000
int main(void){
  int i;
  int j;
  int k;

  int n;
  double rand;
  double suma;
  double *arreglo;

  double ave;
  double std;
  
  arreglo = malloc(m*sizeof(double));
  for (i=1;i<6;i++){
    n = i*20;
    ave = 0;
    std = 0;
    for (j=0;j<m;j++){
      srand48(m*i + j);
      suma = 0;
      for (k=0;k<n;k++){
	rand = drand48();
	suma = suma + rand;
      }
      arreglo[j] = suma;
    }
    for (j=0;j<m;j++){
      ave = ave + (arreglo[j]/m);
    }
    for (j=0;j<m;j++){
      std = std + pow((ave - arreglo[j]),2)/m;
    }
    std = pow(std,0.5);
    printf("%f %f\n",ave,std);
  }
  return 0;
}
