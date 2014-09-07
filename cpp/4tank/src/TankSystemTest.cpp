//
// title: TankSystemController.cpp
// by: Brian Kim
// description: driver program for the tank system
//

#include "TankSystem.hpp"
#include "Types.h"
#include "Constants.h"
#include <cstdio>
#include <cstring>
#include <cstdlib>

#define DEFAULT_LOOP_SIZE 10 

void printf_empty_line()
{
  printf( "--------------------------------------------------------\n" );
}

int main( int argc, char *argv[] )
{
  int n;
  if (argc >= 2)
  {
    n = atof( argv[1] );
  }
  else n = DEFAULT_LOOP_SIZE;

  // define the tank information
  TankInfo top = TankInfo_init( DEFAULT_LARGE_TANK_RADIUS, DEFAULT_LARGE_TANK_HEIGHT, 
                                DEFAULT_DRAIN_RADIUS, DEFAULT_DRAIN_HEIGHT,
                                35);
  TankInfo bottom = top;
  bottom.tank_radius = DEFAULT_SMALL_TANK_RADIUS;
  bottom.tank_height = DEFAULT_SMALL_TANK_HEIGHT;

  // define the tank system information
  TankSystemInfo system_info = TankSystemInfo_init( top, top, bottom, bottom );

  // define the pump information
  PumpInfo pump = PumpInfo_init( DEFAULT_PUMP_RADIUS, DEFAULT_PUMP_VELOCITY, DEFAULT_PUMP_RATIO );

  // define the system
  TankSystem system( system_info, pump, pump );
  if (DEBUG) 
    printf( "system is init: \n" ); system.print( 1 ); 

  for (int i = 0; i < n ; i++)
  {
    printf_empty_line();
    printf( "loop #%d\n", i+1 );

    system.step();
    system.print( 1 ); /* ZZ: print should take in an argument of how many tabs */;


    printf_empty_line();
  }

  return 0;
}
