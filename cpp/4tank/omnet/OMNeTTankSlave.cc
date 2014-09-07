//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2003 Ahmet Sekercioglu
// Copyright (C) 2003-2008 Andras Varga
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

#include <string.h>
#include <omnetpp.h>
#include <stdlib.h>
#include <time.h>

#include "OMNeTTankSystem_m.h"

#include "TankSystem.hpp"
#include "Types.h"

class OMNeTTankSlave : public cSimpleModule
{
  private:
    TankSystem four_tank;
    cMessage *clock_msg;
    int clock;

  protected:
    virtual void initialize();
    // virtual void updateDisplay(); 
    /* ZZ: using printf... */

    virtual void handleMessage( cMessage * );
    void parseCommand( OMNeTTankSystemMsg * );
};

Define_Module(OMNeTTankSlave);

void OMNeTTankSlave::initialize()
{
  // top-left 
  double tl_tank_radius  = par( "tl_tank_radius" ).doubleValue();
  double tl_tank_height  = par( "tl_tank_height" ).doubleValue();
  double tl_drain_radius = par( "tl_drain_radius" ).doubleValue();
  double tl_drain_height = par( "tl_drain_height" ).doubleValue();
  double tl_water_volume = par( "tl_water_volume" ).doubleValue();

  // top-right
  double tr_tank_radius  = par( "tr_tank_radius" ).doubleValue();
  double tr_tank_height  = par( "tr_tank_height" ).doubleValue();
  double tr_drain_radius = par( "tr_drain_radius" ).doubleValue();
  double tr_drain_height = par( "tr_drain_height" ).doubleValue();
  double tr_water_volume = par( "tr_water_volume" ).doubleValue();

  // bottom-left 
  double bl_tank_radius  = par( "bl_tank_radius" ).doubleValue();
  double bl_tank_height  = par( "bl_tank_height" ).doubleValue();
  double bl_drain_radius = par( "bl_drain_radius" ).doubleValue();
  double bl_drain_height = par( "bl_drain_height" ).doubleValue();
  double bl_water_volume = par( "bl_water_volume" ).doubleValue();

  // bottom-right
  double br_tank_radius  = par( "br_tank_radius" ).doubleValue();
  double br_tank_height  = par( "br_tank_height" ).doubleValue();
  double br_drain_radius = par( "br_drain_radius" ).doubleValue();
  double br_drain_height = par( "br_drain_height" ).doubleValue();
  double br_water_volume = par( "br_water_volume" ).doubleValue();

  // left pump
  double left_pump_radius = par( "left_pump_radius" ).doubleValue();
  double left_velocity    = par( "left_velocity" ).doubleValue();
  double left_valve_ratio = par( "left_valve_ratio" ).doubleValue();

  // right pump
  double right_pump_radius = par( "right_pump_radius" ).doubleValue();
  double right_velocity    = par( "right_velocity" ).doubleValue();
  double right_valve_ratio = par( "right_valve_ratio" ).doubleValue();

  // create the tank infos
  TankInfo tl_info = TankInfo_init( tl_tank_radius, tl_tank_height, tl_drain_radius, tl_drain_height, tl_water_volume );
  TankInfo tr_info = TankInfo_init( tr_tank_radius, tr_tank_height, tr_drain_radius, tr_drain_height, tr_water_volume );
  TankInfo bl_info = TankInfo_init( bl_tank_radius, bl_tank_height, bl_drain_radius, bl_drain_height, bl_water_volume );
  TankInfo br_info = TankInfo_init( br_tank_radius, br_tank_height, br_drain_radius, br_drain_height, br_water_volume );
  TankSystemInfo sys_info = TankSystemInfo_init( tl_info, tr_info, bl_info, br_info );
  
  // create the pump infos
  PumpInfo left_pump = PumpInfo_init( left_pump_radius, left_velocity, left_valve_ratio );
  PumpInfo right_pump = PumpInfo_init( right_pump_radius, right_velocity, right_valve_ratio );

  // init the four tank system
  four_tank = TankSystem( sys_info, left_pump, right_pump );

  // set up the clock
  clock = 0;
  clock_msg = new cMessage( "clock" );
  send( clock_msg, "clock_out" );

  printf( "Networked 4 Tank System Simulation Started:\n" );
}

void OMNeTTankSlave::handleMessage(cMessage *msg)
{
  if (msg == clock_msg)
  {
    four_tank.step();
    printf( "clock: %d\n", ++clock );
    four_tank.print(1);

    send( clock_msg, "clock_out" );
  }
  else
  {
    OMNeTTankSystemMsg *cmd_msg = check_and_cast<OMNeTTankSystemMsg *>(msg);
    parseCommand( cmd_msg );
  }
}

void OMNeTTankSlave::parseCommand( OMNeTTankSystemMsg *msg )
{
  double val = msg->getValue();
  int key = msg->getKey();
  int index = msg->getIndex();
  if (msg->getSetTank() == true) // tank command
  {
    switch( getIndex() )
    {
      case 1:
        four_tank.getTopLeftTank()->setValve( val );
        printf( "top left drain valve set to: %4.3f\n", val );
        break;
      case 2: 
        four_tank.getBottomLeftTank()->setValve( val );
        printf( "bottom left drain valve set to: %4.3f\n", val );
        break;
      case 3:
        four_tank.getTopRightTank()->setValve( val );
        printf( "top right drain valve set to: %4.3f\n", val );
        break;
      
      case 4:
        four_tank.getBottomRightTank()->setValve( val );
        printf( "bottom right drain valve set to: %4.3f\n", val );
        break;
      default:
        return;
    }
  }
  else // pump command
  {
    if (index == 1) // left
      if (key == PumpCommandSetValveRatio) // set valve ratio
      {
        four_tank.setLeftPumpValveRatio( val );
        printf( "left pump valve ratio set to: %4.3f\n", val );
      }
      else // set velocity
      {
        four_tank.setLeftPumpVelocity( val );
        printf( "left pump velocity set to: %4.3f\n", val );
      }

    else // right
      if (msg->getKey() == PumpCommandSetValveRatio) // set valve ratio
      {
        four_tank.setRightPumpValveRatio( val );
        printf( "right pump valve ratio set to: %4.3f\n", val );
      }
      else // set velocity
      {
        four_tank.setRightPumpVelocity( val );
        printf( "right pump velocity set to: %4.3f\n", val );
      }
  }
}

