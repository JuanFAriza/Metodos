#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 1000000000

int main(void){
  int i;
  float x,y;
  float Nhits;
  float pi;

  srand48(1);
  for (i=0;i<N;i++){
    x = 2*drand48() - 1;
    y = 2*drand48() - 1;
    if (pow(x,2) + pow(y,2) < 1){
      Nhits = Nhits + 1;
    }
  }
  pi = 4*Nhits/N;
  printf("Pi es %f\n",pi);
  return(1);
}
