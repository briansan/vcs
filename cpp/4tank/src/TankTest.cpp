//
// title: TankTest.cpp
// by: Brian Kim
// description: unit testing for the tank controller
//

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include "TankController.hpp"

int main( int argc, char **argv )
{
  if (argc == 2 && (!strcmp( argv[1], "-h" ) || !strcmp( argv[1], "--help")))
  {
    fprintf( stdout, "TankTest: usage: ./TankTest <number of runs> <tank_radius> <tank_height> <drain_radius> <drain_height> <init_water_volume> <water flow> <change in valve>\n" );
    return 1;
  }

  const char *n_s            = argc >= 2 ? argv[1] : "20";
  const char *tank_radius_s  = argc >= 3 ? argv[2] : "5.0";
  const char *tank_height_s  = argc >= 4 ? argv[3] : "10.0";
  const char *drain_radius_s = argc >= 5 ? argv[4] : "1.0";
  const char *drain_height_s = argc >= 6 ? argv[5] : "2.0";
  const char *init_water_s   = argc >= 7 ? argv[6] : "830.0";
  const char *d_water_in_s   = argc >= 8 ? argv[7] : "3.0";
  const char *d_valve_s      = argc >= 9 ? argv[8] : "0.01";
 
  double n            = atof( n_s );
  double tank_radius  = atof( tank_radius_s );
  double tank_height  = atof( tank_height_s );
  double drain_radius = atof( drain_radius_s );
  double drain_height = atof( drain_height_s );
  double init_water   = atof( init_water_s );
  double d_water_in   = atof( d_water_in_s );
  double d_valve      = atof( d_valve_s );

  TankInfo info = TankInfo_init( tank_radius, tank_height, drain_radius, drain_height, init_water );
  TankController tank(info);
  
  tank.setWaterIn( d_water_in );

  for( int i = 0; i < n; i++ )
  {
    tank.step();
    tank.print();
    
    tank.setValve( tank.getValve() - d_valve );
  }
  
  return 0;
}
