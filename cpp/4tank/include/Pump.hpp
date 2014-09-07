//
// title: Pump.hpp
// by: Brian Kim
// description: the pump that distributes water to 
//  the tanks
//
#ifndef _PUMP_H_
#define _PUMP_H_

#include <stdio.h>
#include "Constants.h" 

/* ZZ: does not have any pipe lengths */
class Pump
{
  // 
  // instance variables
  //
  private:
    double _velocity, _pipeRadius, _valveRatio; // givens
    double _area; // calculated

  // 
  // constructor methods
  //
  public:
    Pump( double pipe_radius, double velocity, double valve_ratio ) 
    { 
      if (DEBUG) 
      {
        printf( "Pump: debug: Pump constructor called\n"); 
        printf( "arg vals:\npipe_radius = %4.3f\nvelocity = %4.3f\nvalve_ratio = %4.3f\n",
                            pipe_radius,         velocity,         valve_ratio );
      }
            
      _pipeRadius = pipe_radius; 
      _area = PI*pipe_radius*pipe_radius; 

      setVelocity( velocity ); 
      setValveRatio( valve_ratio ); 
      
    }
    Pump( double pipe_radius, double velocity ) { Pump( pipe_radius, velocity, 1.0 ); }
    Pump( double pipe_radius ) { Pump( pipe_radius, 0.0 ); }
    Pump( PumpInfo info )
    { 
      _pipeRadius = info.pipe_radius;
      _area = PI*info.pipe_radius*info.pipe_radius; 
      _velocity = info.velocity;
      _valveRatio = info.valve_ratio ; 
    }
    Pump() { Pump( 1.0 ); }


  //
  // accessor methods
  //
    double getVelocity() { return _velocity; }
    void setVelocity( double x ) { if ( x > 0 ) _velocity = x; }

    double getPipeRadius() { return _pipeRadius; }

    double getValveRatio() { return _valveRatio; }
    void setValveRatio( double x ) { if ( x > 0 && x <= 1.0) _valveRatio = x; }

    double getArea() { return _area; }

    double getFlowRate() { return _area*_velocity; }

    void print()
    {
      printf( "velocity: %4.3f, valve_ratio: %4.3f\n", getVelocity(), getValveRatio() );
    }
};

#endif
