#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N (int)100
#define xi 0.0
#define xf 20.0
#define a 7.5
#define b 13.5
#define c 123.0

int main(void){
  int i;
  double x,y;
  double delta = (xf - xi)/N;
  srand48(1);

  for (i=0;i<N;i++){
    x = i*delta + (drand48()*2*delta - delta)*0.3;
    y = a*pow(x,2) + b*x + c + (drand48()*2 - 1)*50;
    printf("%f %f\n",x,y);
  }
  return 0;
}
