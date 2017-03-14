#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define n_points 1000

int main(void){
  int i;
  float *x;
  float *u_initial;
  float *u_future;
  float *u_past;
  float *u_present;
  float delta_x;
  float r;
  float delta_t = 0.0005;
  float c = 1.0;

  x = malloc(n_points*sizeof(float));
  u_initial = malloc(n_points*sizeof(float));
  u_future = malloc(n_points*sizeof(float));
  u_past = malloc(n_points*sizeof(float));
  u_present = malloc(n_points*sizeof(float));

  for (i=0;i<n_points;i++){
    x[i] = i*(1.0-0.0)/(n_points-1);
  }
  for (i=0;i<n_points;i++){
    u_initial[i] = exp(-(pow(x[i]-0.3,2))/0.01);
  }
  for (i=0;i<n_points;i++){
    u_future[i] = 0;
  }

  delta_x = x[1] - x[0];
  r = c*delta_t/delta_x;

  u_initial[0] = 0;
  u_initial[n_points-1] = 0;
  u_future[0] = 0;
  u_future[n_points-1] = 0;

  for (i=1;i<n_points-1;i++){
    u_future[i] = u_initial[i] + (pow(r,2)/2.0)*(u_initial[i+1] - 2.0*u_initial[i] + u_initial[i-1]);
    printf("%f\n",u_future[i]);
  }

  for (i=0;i<n_points;i++){
    u_past[i] = u_initial[i];
  }
  for (i=0;i<n_points;i++){
    u_present[i] = u_future[i];
  }

  return 0;
}
