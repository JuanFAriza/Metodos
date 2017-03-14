#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define Pi 3.141592653589793
#define N (int)1000
#define t_ini (double)0
#define t_fin (double)1
#define delta_t 0.01

static int n = 1 + (int)((t_fin - t_ini)/delta_t);

void w(double *t, double *wt, int j);
double normRand(double aleat1, double aleat2);

int main(void){
  int iter,i;
  double *t,*wt,*u;

  t = malloc(n*sizeof(double));
  wt = malloc(n*sizeof(double));
  u = malloc(n*sizeof(double));

  for (i=0;i<n;i++){
    wt[i] = u[i] = 0;
    t[i] = i*delta_t;
  }

  for (iter=0;iter<N;iter++){
    w(t,wt,iter);
    for (i=0;i<n;i++){
      u[i] = u[i] + (1/(float)N)*exp(t[i] - 0.5*wt[i]);
    }
  }
  for (i=0;i<n;i++){
    printf("%f\n",u[i]);
  }
  return 0;
}

void w(double *t, double *wt, int j){
  int i;
  srand48(1);
  wt[0] = 0;
  for (i=1;i<n;i++){
    wt[i] = wt[i-1] + pow(delta_t,0.5)*normRand(drand48(),drand48());
  }
}

double normRand(double aleat1, double aleat2){
  double phi = 2*Pi*aleat1;
  double gamma = -log(aleat2);
  double r = pow(2*gamma,0.5);
  return(r*cos(phi));
}
