#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define N (int)pow(10,6)
#define a0 (double)7.5
#define b0 (double)13.5
#define c0 (double)123
#define delta_a (double)0.01
#define delta_b (double)0.01
#define delta_c (double)0.01

static int lineas = 0;

double probabilidad(double *x , double *y, double aold, double bold, double cold, double anew, double bnew, double cnew);

int main(void){
  int i,iter;
  double *a,*b,*c,anew,bnew,cnew,alpha,u,amean,bmean,cmean;
  amean = bmean = cmean = 0;
  
  FILE *ptr_file;
  char buf[1000],*fragmento;
  double val;
  
  ptr_file = fopen("datos.dat", "r");
  
  if (!ptr_file){
    return 1;
  }
  i = 0;
  while (fgets(buf,1000,ptr_file)!=NULL){
    i++;
  }
  lineas = i;
  double *x;
  double *y;

  x = malloc(lineas*sizeof(double));
  y = malloc(lineas*sizeof(double));

  a = malloc(N*sizeof(double));
  b = malloc(N*sizeof(double));
  c = malloc(N*sizeof(double));

  ptr_file = fopen("datos.dat", "r");
  i = 0;
  while (fgets(buf,1000,ptr_file)!=NULL){
    fragmento = strtok(buf," ");
    val = atof(fragmento);
    x[i] = val;
    fragmento = strtok(NULL," ");
    val = atof(fragmento);
    y[i] = val;
    i++;
  }
  fclose(ptr_file);

  srand48(1);
  a[0] = a0;
  b[0] = b0;
  c[0] = c0;
  for (iter=1;iter<N;iter++){
    if (iter%10000 == 0){
      srand48(iter/10000);
    }
    anew = a[iter-1] + (drand48() - 0.5)*2*delta_a;
    bnew = b[iter-1] + (drand48() - 0.5)*2*delta_b;
    cnew = c[iter-1] + (drand48() - 0.5)*2*delta_c;
    alpha = probabilidad(x,y,a[iter-1],b[iter-1],c[iter-1],anew,bnew,cnew);
    u = drand48();
    if (u < alpha){
      a[iter] = anew;
      b[iter] = bnew;
      c[iter] = cnew;
    }
    else{
      a[iter] = a[iter-1];
      b[iter] = b[iter-1];
      c[iter] = c[iter-1];
    }
  }
  for (iter=0;iter<N;iter++){
    amean = amean + (1/(float)N)*a[iter];
    bmean = bmean + (1/(float)N)*b[iter];
    cmean = cmean + (1/(float)N)*c[iter];
  }
  printf("%f %f %f\n",amean,bmean,cmean);
  return 0;
}

double probabilidad(double *x , double *y, double aold, double bold, double cold, double anew, double bnew, double cnew){
  int i;
  double x2old,x2new;
  for (i=0;i<lineas;i++){
    x2old = pow(y[i] - (aold*pow(x[i],2) + bold*x[i] + cold),2);
    x2new = pow(y[i] - (anew*pow(x[i],2) + bnew*x[i] + cnew),2);
  }
  return(exp(0.5*(x2old-x2new)));
}
