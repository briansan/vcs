//
// title = TankSystem.c
// by = Brian Kim
// description = implementing the simulation of the 4 tank system
//

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "TankSystem.h"

double freefall_velocity( double ); // cm / s

int main( int argc, char *argv[] )
{
  double v1 = 0.8, v2 = 0.8;    // tank speeds (input)
  double h1, h2, h3, h4;       // tank levels (output)

  double y1 = DEFAULT_Y1;  // ratio of water diverted to t1 from t3 
  double y2 = DEFAULT_Y2;  // ratio of water diverted to t2 from t4
  
  double k1 = DEFAULT_K1;      // what is k...constant?
  double k2 = DEFAULT_K2;

  double dh1, dh2, dh3, dh4;   // changes in water height of the tanks
  int i = 0, n = 1000;         // number of iterations

  if (argc == 3)
  {
    v1 = atof(argv[1]);
    v2 = atof(argv[2]);
  }

  printf( " tank 1 | tank 2 | tank 3 | tank 4\n" );
  // each column has a width of 8

  while( i < n )
  {
    // output tank heights
    printf( "%7.5f %7.5f %7.5f %7.5f\n", t1.water_height, t2.water_height, t3.water_height, t4.water_height );

    // dh1/dt
    dh1 = -( t1.drain_area / t1.tank_area ) * freefall_velocity( t1.water_height );
    dh1 += ( t3.drain_area / t1.tank_area ) * freefall_velocity( t3.water_height );
    dh1 += y1 * k1 / t1.tank_area * v1;

    // dh2/dt
    dh2 = -( t2.drain_area / t2.tank_area ) * freefall_velocity( t2.water_height );
    dh2 += ( t4.drain_area / t2.tank_area ) * freefall_velocity( t4.water_height );
    dh2 += y2 * k2 / t2.tank_area * v2;

    // dh3/dt
    dh3 = -( t3.drain_area / t3.tank_area ) * freefall_velocity( t3.water_height );
    dh3 += ( 1 - y2 ) * k2 / t3.tank_area * v2;

    // dh4/dt
    dh4 = -( t4.drain_area / t4.tank_area ) * freefall_velocity( t4.water_height );
    dh4 += ( 1 - y1 ) * k1 / t4.tank_area * v1;

    // change the water heights
    t1.water_height += dh1;
    t2.water_height += dh2;
    t3.water_height += dh3;
    t4.water_height += dh4;

    i++;
  }
}

double freefall_velocity( double height ) { return sqrt( 2 * GRAVITY * height ); }
