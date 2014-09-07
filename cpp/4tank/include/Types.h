//
// title: Types.h
// by: Brian Kim
// description: type definition of tank information
//

#ifndef _TANKINFO_H_
#define _TANKINFO_H_

#ifdef C_PLUS_PLUS
extern C {
#endif
  
#include "Constants.h" 

/**
 *
 *
 */
typedef struct _TankInfo
{
  // all using cm
  double tank_radius, tank_height, drain_radius, drain_height, init_water_volume;
} TankInfo;

/**
 *
 *
 */
TankInfo TankInfo_init( double tank_radius, double tank_height, 
                        double drain_radius, double drain_height, 
                        double init_water_volume );

/**
 *
 *
 */
typedef struct _TankSystemInfo
{
  TankInfo tanks[4];
} TankSystemInfo;

/**
 *
 *
 */
TankSystemInfo TankSystemInfo_init( TankInfo tl, TankInfo tr, TankInfo bl, TankInfo br );

/**
 *
 *
 */
typedef struct _PumpInfo
{
  double pipe_radius;
  double velocity;
  double valve_ratio;
} PumpInfo;

/**
 *
 *
 */
PumpInfo PumpInfo_init( double pipe_radius, double velocity, double valve_ratio );

/**
 *
 *
 */
typedef enum _PumpCommand
{
  PumpCommandSetValveRatio,
  PumpCommandSetVelocity
} PumpCommand;

#ifdef C_PLUS_PLUS
}
#endif

#endif // _TANKINFO_H_
