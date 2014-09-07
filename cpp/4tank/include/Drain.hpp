//
// title: Drain.hpp
// by: Brian Kim
// description: class declaration for the drain that 
//  allows water to flow out of a tank.
// note:
//  for our purposes, a drain will be cylindrical
//
#ifndef _DRAIN_H_
#define _DRAIN_H_

#include "Tank.hpp"

class Drain : public Tank
{
  //
  // constructor methods
  //
  public:
    Drain( double radius, double height, double valve ) : Tank( radius, height, valve ) {}
    Drain( double radius, double height )               : Tank( radius, height ) {}
    Drain()                                             : Tank() {}
  
  // 
  // utility methods
  //
    void setValve( double valve ) { if (_valve >= 0.0 && _valve <= 1.0) _valve = valve; }

};

#endif // _DRAIN_H_
