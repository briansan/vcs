//
// title: Tank.h
// by: Brian Kim
// description: class declaration for the Tank
//
// note: this is where keeping your units straight will 
//   really come in handy...we recommend cc (cubic cm)
//

#ifndef _TANK_H_
#define _TANK_H_

#include "Constants.h"
#include "Cylinder.hpp"

class Tank : public Cylinder
{
  //
  // member variables
  //

  protected:
    double _valve;  // range = [0.0, 1.0]
    /* ZZ: technically, valve should be its own class that incrementally changes 
    its open/closed-ness to make our simulation more realistic */
    
  // 
  // constructor methods
  //

  public:
    Tank( double radius, double height, double valve ) :
      Cylinder( radius, height )                      // calling cylinder's constructor
      { _valve = valve; }
    Tank( double radius, double height ) 
      { Tank( radius, height, 1.0 ); }
    Tank() 
      { Tank( 6.0, 10.0 ); }

  // 
  // accessor methods
  //

    // valve 
    double getValve()   { return _valve; }

};

#endif // _TANK_H_

