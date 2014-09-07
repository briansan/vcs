//
// title = TankSystem.h
// by = Brian Kim
// description = type definitions necessary to implement 
//   a four-tank system
//

#define GRAVITY 981     // cm/s2

#define DEFAULT_K1 5.51 // cm3/s
#define DEFAULT_K2 6.58 // cm3/s

#define DEFAULT_Y1 0.333
#define DEFAULT_Y2 0.307

#define TANK_AREA_LG 32   // cm2
#define TANK_AREA_SM 28   // cm2

#define DRAIN_AREA_LG 0.071  // cm2
#define DRAIN_AREA_SM 0.057  // cm2

typedef struct
{
  double tank_area, drain_area, water_height;
          /* cm2 */ /* cm2 */   /*  cm   */
} Tank;

typedef struct
{
  Tank t1, t2, t3, t4;
} TankSystem;

TankSystem *TankSystem_init();
void TankSystem_cleanup();

Tank t1 = { TANK_AREA_LG, DRAIN_AREA_LG, 14.1 };
Tank t2 = { TANK_AREA_LG, DRAIN_AREA_LG, 11.2 };
Tank t3 = { TANK_AREA_SM, DRAIN_AREA_SM, 7.2 };
Tank t4 = { TANK_AREA_SM, DRAIN_AREA_SM, 4.7 };

