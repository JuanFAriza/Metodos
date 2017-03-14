#include <stdio.h>
#define m 134456
#define n 8121
#define k 28411
#define N 1000000

double generar(int *idum);

int main(void){
  int i;
  int idum = 1;
  double ran;
  for (i=0;i<N;i++){
    ran = generar(&idum);
    printf("%f\n",ran);
  }
  return 1;
}

double generar(int *idum){
  double ran;
  *idum = (*idum*n + k)%m;
  ran = *idum/(double)m;
  return(ran);
}
