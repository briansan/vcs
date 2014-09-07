//
// title = Cylinder.hpp
// by = Brian Kim
// description = class declaration for a cylinder
//   which happens to be the shape of our tanks
// note:
//   this class is defined unitlessly meaning
//   that the unit you use is the unit you get
//

#ifndef _CYLINDER_H_
#define _CYLINDER_H_

#include "Constants.h"

class Cylinder
{
  //
  // instance variables
  //
  private:
    double _radius, _height; // givens
    double _area, _circumference, _surfaceArea, _volume; // calculated

  // 
  // constructor methods
  //
  public:
    Cylinder( double radius, double height) 
      { 
        _radius = radius; _height = height; 
        _area = PI*radius*radius;
        _circumference = 2*PI*radius;
        _surfaceArea = _circumference*_height;
        _volume = _area*_height;
      }
    Cylinder() 
      { Cylinder( 6.0, 10.0 ); } // just using random values...

  // 
  // utility methods
  //
  double getArea()          { return _area; }
  double getCircumference() { return _circumference; }
  double getHeight()        { return _height; }
  double getRadius()        { return _radius; } 
  double getSurfaceArea()   { return _surfaceArea; }
  double getVolume()        { return _volume; }
};

#endif // _CYLINDER_H_
