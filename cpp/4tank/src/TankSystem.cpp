//
// title: TankSystem.cpp
// by: Brian Kim
// description: class definition of the 4 tank system
//  

#include "TankSystem.hpp"
#include <cstdio>

void TankSystem::step()
{
  //
  // check for updated inputs
  //
  

  // dummy variables
  double left_rate = _leftPump.getFlowRate();
  double left_ratio = _leftPump.getValveRatio();
  double right_rate = _rightPump.getFlowRate();
  double right_ratio = _rightPump.getValveRatio();

  //
  // from top to bottom...
  //

  // get the top tank flow rates
  double tl_flow = right_rate * right_ratio;
  double tr_flow = left_rate * left_ratio;

  // set the top tank water in flow rates
  _tlTank.setWaterIn( tl_flow );
  _trTank.setWaterIn( tr_flow );

  // step the top tanks
  _tlTank.step();
  _trTank.step();

  // get the bottom tank flow rates
  double bl_flow = _tlTank.getWaterOut() + left_rate * (1.0 - left_ratio);
  double br_flow = _trTank.getWaterOut() + right_rate * (1.0 - right_ratio);

  // set the bottom tank water in flow rates
  _blTank.setWaterIn( bl_flow );
  _brTank.setWaterIn( br_flow );

  // step the bottom tanks
  _blTank.step();
  _brTank.step();
}
