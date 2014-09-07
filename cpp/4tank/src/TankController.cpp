//
// title: TankController.cpp
// by: Brian Kim
// description: class definition of the tank controller
//

#include "TankController.hpp"
#include "Constants.h"

TankController::TankController()
{
}


TankController::TankController( TankInfo info )
{
  // init drain
  _drain = Drain( info.drain_radius, info.drain_height, 1.0 );

  // calculate the openness of the tank's valve
  double tank_volume = PI * info.tank_radius * info.tank_radius;
  double tank_valve = _drain.getVolume() / tank_volume;

  // init tank
  _tank = Tank( info.tank_radius, info.tank_height, tank_valve );

  // init water 
  _waterVolume = info.init_water_volume;
  _waterIn = 0.0;
  _waterOut = 0.0;

  // init drain water volume
  if (_waterVolume)
    _drainWaterVolume = _waterVolume > _drain.getVolume() ? _drain.getVolume() : _waterVolume;
  else
    _drainWaterVolume = 0.0;

  // init state
  _state = _waterVolume ? TankStateStatic : TankStateEmpty;
}


double TankController::getWaterHeight() 
{
  double tank_radius = _tank.getRadius();
  
  return (_waterVolume - _drainWaterVolume) / (PI * tank_radius * tank_radius);
}

bool TankController::isDraining() { return _waterOut - _waterIn > 0.001; }
bool TankController::isEmpty()    { return _waterVolume < 0.00001; }
bool TankController::isFilling()  { return _waterOut - _waterIn < 0.001; }
bool TankController::isFull()     { return getTotalVolume() - _waterVolume < 0.000001; }
bool TankController::isOverflow() { return (isFull() && isFilling()) || (_waterVolume > getTotalVolume()); }
bool TankController::isStatic()   { return !isFull() && !isFilling(); }

void TankController::updateState() 
{   
  if      (isEmpty())    _state = TankStateEmpty;
  else if (isOverflow()) _state = TankStateOverflow;
  else if (isFull())     _state = TankStateFull;
  else if (isFilling())  _state = TankStateFilling;
  else if (isDraining()) _state = TankStateDraining;
  else                   _state = TankStateStatic;
}

void TankController::step()
{
  // dummy variables
  double drain_volume = _drain.getVolume();

  // temporary water volume 
  double t_waterVolume = _waterVolume + _waterIn;

  // only set water volume if tank isn't full
  if (_state != TankStateFull) _waterVolume = t_waterVolume;

  // only update water out if there is water
  if (_waterVolume)
  {
    _waterOut =  drain_volume * _drain.getValve();

    _waterVolume -= _waterOut;
    _drainWaterVolume -= _waterVolume > drain_volume ? 0 : _waterOut;

    // make sure certain values aren't < 0
    _waterVolume = _waterVolume > 0 ? _waterVolume : 0;
    _drainWaterVolume = _drainWaterVolume > 0 ? _drainWaterVolume : 0;
  }

  // update the state
  updateState();
}

