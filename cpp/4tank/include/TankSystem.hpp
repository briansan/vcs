//
// title = TankSystem.hpp
// by = Brian Kim
// description = class declaration for the tank system
//
#ifndef _TANK_SYSTEM_H_
#define _TANK_SYSTEM_H_

#include <cstdio>
#include "TankController.hpp"
#include "Pump.hpp"
#include "Types.h"

class TankSystem
{
  //
  // instance variables
  //
  private:
    TankController _tlTank;
    TankController _trTank;
    TankController _blTank;
    TankController _brTank;

    Pump _leftPump;
    Pump _rightPump;

  // 
  // constructor methods
  //
  public:
    TankSystem( TankSystemInfo info, PumpInfo left, PumpInfo right ) :
      _tlTank( info.tanks[0] ), _trTank( info.tanks[1] ),
      _blTank( info.tanks[2] ), _brTank( info.tanks[3] ),
      _leftPump( left ), _rightPump( right ) 
      { }
    TankSystem() 
    {
      // _tlTanks( 
    }
    /*
      _tlTank(info.tanks[0]), _trTank(info.tanks[1]),
      _blTank(info.tanks[2]), _brTank(info.tanks[3]),
      _leftPump(left), _rightPump(right) {}
    */
    /* ZZ: I HATE C++
    TankSystem( TankSystemInfo info, double pipe_radius )
    {
      PumpInfo p_info = PumpInfo_init( pipe_radius, 0.0, 1.0 );
      TankSystem( info, p_info, p_info );
    }

    TankSystem( TankSystemInfo info )
    {
      TankSystem( info, 1.0 );
    }
    TankSystem(); 
    */

  //
  // accessor methods
  //
    TankController *getTopLeftTank()     { return &_tlTank; }
    TankController *getTopRightTank()    { return &_trTank; }
    TankController *getBottomLeftTank()  { return &_blTank; }
    TankController *getBottomRightTank() { return &_brTank; }

    Pump *getLeftPump()  { return &_leftPump; }
    Pump *getRightPump() { return &_rightPump; }

    void setLeftPumpValveRatio( double r ) { _leftPump.setValveRatio( r ); }
    void setLeftPumpVelocity( double v ) { _leftPump.setVelocity( v ); }

    void setRightPumpValveRatio( double r ) { _rightPump.setValveRatio( r ); }
    void setRightPumpVelocity( double v ) { _rightPump.setVelocity( v ); }
    
  // 
  // utility methods
  //
    void step();
    void print( int n_tabs )
    {
      print_n_tabs( n_tabs ); printf( "t1: " ); getTopLeftTank()->print();
      print_n_tabs( n_tabs ); printf( "tr: " ); getTopRightTank()->print();
      print_n_tabs( n_tabs ); printf( "b1: " ); getBottomLeftTank()->print();
      print_n_tabs( n_tabs ); printf( "br: " ); getBottomRightTank()->print();

      print_n_tabs( n_tabs ); printf( "left pump: " ); getLeftPump()->print();
      print_n_tabs( n_tabs ); printf( "right pump: " ); getRightPump()->print();

    }

    void print_n_tabs( int n )
    {  for (int i = 0; i < n; i++) putchar( '\t' ); }
};

#endif // _TANK_SYSTEM_H_
