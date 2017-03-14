#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define Pi 3.141592653589793
#define Sigma 1
#define delta 0.2
#define N (int)pow(10,6)
#define x0 1

double p(double x);

int main(void){
  int i;
  double x = x0;
  double xnew;
  double alpha;
  double u;
  srand48(1);
  printf("%f\n",x);
  for (i=0;i<N;i++){
    xnew = x + drand48()*2*delta - delta;
    if (1 < p(xnew)/p(x)){
      alpha = 1;
    }
    else{
      alpha = p(xnew)/p(x);
    }
    u = drand48();
    if (u < alpha){
      x = xnew;
    }
    printf("%f\n",x);
  }
  return 0;
}

double p(double x){
  return((1.0/(Sigma*pow(2*Pi,0.5)))*exp(-pow(x,2)/(2*pow(Sigma,2))));
}
