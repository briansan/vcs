//
// title: TankController.hpp
// by: Brian Kim
// description: class declaration of tank controller
//  manages the water flow in the tank and drain
//
#ifndef _TANKCONTROLLER_H_
#define _TANKCONTROLLER_H_

#include <stdio.h>
#include "Constants.h"
#include "Types.h"
#include "Tank.hpp"
#include "Drain.hpp"

typedef enum _TankState
{
  TankStateEmpty,
  TankStateDraining,
  TankStateStatic,
  TankStateFilling,
  TankStateFull,
  TankStateOverflow
} TankState;

class TankController
{
  //
  // instance variables
  //
  private:
    Tank _tank;
    Drain _drain;
    TankState _state;
  
    // water data
    double _waterIn;
    double _waterVolume;
    double _waterOut;

    double _drainWaterVolume;
    
  // 
  // constructor methods
  //
  public:
    TankController( TankInfo );
    TankController();

  //
  // accessor methods
  //
    double getTotalVolume() { return _tank.getVolume() + _drain.getVolume(); }

    void setWaterIn( double x ) { _waterIn = x; }
    double getWaterHeight();
    double getWaterVolume() { return _waterVolume; }
    double getWaterOut()    { return _waterOut; }

    double getValve() { return _drain.getValve(); }
    void setValve( double valve ) { _drain.setValve( valve ); }

  // 
  // utility methods
  // 
    // print method

    void print()
    {
      printf( "state: %8s, ", state2string());
      printf( "water volume: %6.3f, ", _waterVolume);
      printf( "water height: %6.3f, ", getWaterHeight());
      printf( "water in: %6.3f, ", _waterIn);
      printf( "water out: %6.3f, ", _waterOut);
      printf( "valve: %3.2f", _drain.getValve());
      printf( "\n" );
    }

    // refresh values
    void step(); /* ZZ: assumes 1 second */

    // state methods
    bool isDraining();
    bool isEmpty();
    bool isFilling();
    bool isFull();
    bool isOverflow();
    bool isStatic();

    const char *state2string()
    {
      switch (_state)
      {
        case TankStateEmpty: return "Empty";
        case TankStateDraining: return "Draining";
        case TankStateOverflow: return "Overflow";
        case TankStateFilling: return "Filling";
        case TankStateFull: return "Full";
        case TankStateStatic: return "Static";
        default: return "Unknown";
      }
      return NULL;
    }

  private:
    void updateState();
};

#endif // _TANKCONTROLLER_H_
