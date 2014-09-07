//
// title = Constants.h
// by = Brian Kim
// description = constants used for the 4 tank system
//
#ifndef _CONSTANTS_H_
#define _CONSTANTS_H_

#define DEBUG 1 

#ifndef PI
  #define PI 3.14159
#endif 

//  #define GRAVITY 981     // cm/s2

#define DEFAULT_LARGE_TANK_RADIUS 3.192
#define DEFAULT_LARGE_TANK_HEIGHT 5.0
#define DEFAULT_SMALL_TANK_RADIUS 2.985
#define DEFAULT_SMALL_TANK_HEIGHT 5.0

#define DEFAULT_DRAIN_RADIUS 1.00
#define DEFAULT_DRAIN_HEIGHT 0.50

#define DEFAULT_PUMP_RADIUS 0.838
#define DEFAULT_PUMP_VELOCITY 2.5
#define DEFAULT_PUMP_RATIO 0.333

/* flow rate
#define DEFAULT_K1 5.51 // cm3/s
#define DEFAULT_K2 6.58 // cm3/s

#define DEFAULT_Y1 0.333
#define DEFAULT_Y2 0.307

#define TANK_AREA_LG 32   // cm2
#define TANK_AREA_SM 28   // cm2

#define DRAIN_AREA_LG 0.071  // cm2
#define DRAIN_AREA_SM 0.057  // cm2
*/

#endif // _CONSTANTS_H_
