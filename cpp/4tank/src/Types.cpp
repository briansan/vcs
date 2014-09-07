#include "Types.h"


TankInfo TankInfo_init( double tank_radius,  double tank_height, 
                        double drain_radius, double drain_height, 
                        double init_water_volume )
{ return (TankInfo) { tank_radius, tank_height, drain_radius, drain_height, init_water_volume }; }

TankSystemInfo TankSystemInfo_init( TankInfo tl, TankInfo tr, TankInfo bl, TankInfo br )
{ return (TankSystemInfo){ {tl, tr, bl, br} }; }
    
PumpInfo PumpInfo_init( double pipe_radius, double velocity, double valve_ratio )
{ return (PumpInfo) {pipe_radius,velocity,valve_ratio}; }

