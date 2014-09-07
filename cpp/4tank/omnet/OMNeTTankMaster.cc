//
// title = TankMaster.cc
// by = Brian Kim
// description = definition of the TankMaster module to 
//   1. send commands to the 4 tank system
//   2. read data from the 4 tank system
//

#include <string.h>
#include <omnetpp.h>
#include <stdlib.h>
#include <time.h>

#include <vector>
#include "OMNeTTankSystem_m.h"
#include "Types.h"

class OMNeTTankMaster : public cSimpleModule
{
  protected:
    virtual void initialize();

    virtual OMNeTTankSystemMsg *generateMessage( bool setTank, int index, int key, double val );
    virtual void scheduleCmdAt( OMNeTTankSystemMsg *msg, double delay );
    
    // generate tank cmds
    void setTopLeftTankValve( double x, double t )
      { scheduleCmdAt( generateMessage( true, 1, 0, x ), t); }
    void setTopRightTankValve( double x, double t )
      { scheduleCmdAt( generateMessage( true, 2, 0, x ), t); }
    void setBottomLeftTankValve( double x, double t )
      { scheduleCmdAt( generateMessage( true, 3, 0, x ), t); }
    void setBottomRightTankValve( double x, double t )
      { scheduleCmdAt( generateMessage( true, 4, 0, x ), t); }

    // generate pump cmds
    void setLeftPumpValveRatio( double x, double t )
      { scheduleCmdAt( generateMessage( false, 1, PumpCommandSetValveRatio, x ), t); }
    void setLeftPumpVelocity( double x, double t )
      { scheduleCmdAt( generateMessage( false, 1, PumpCommandSetVelocity, x ), t); }
    void setRightPumpValveRatio( double x, double t )
      { scheduleCmdAt( generateMessage( false, 2, PumpCommandSetValveRatio, x ), t); }
    void setRightPumpVelocity( double x, double t )
      { scheduleCmdAt( generateMessage( false, 2, PumpCommandSetVelocity, x ), t); }
};

Define_Module(OMNeTTankMaster);

void OMNeTTankMaster::initialize()
{
  // arbitrarily decided commands to send to the tank system
  setLeftPumpVelocity( 1.0, 3);
  setRightPumpVelocity( 2.0, 5);

  setLeftPumpValveRatio( 0.5, 7);
  setRightPumpValveRatio( 0.5, 9);
}

OMNeTTankSystemMsg *OMNeTTankMaster::generateMessage( bool setTank, int index, int key, double val ) 
{
  // a generator method to create a fully prepared message for the client to send out to the server
  OMNeTTankSystemMsg *msg = new OMNeTTankSystemMsg;
  msg->setSetTank( setTank );
  msg->setIndex( index );
  msg->setKey( key );
  msg->setValue( val );
  return msg;
}

void OMNeTTankMaster::scheduleCmdAt( OMNeTTankSystemMsg *msg, double delay )
{
  EV << "sending msg val: " <<  msg->getValue() << "\ndelayed to: " << delay << endl;
  sendDelayed( msg, delay, "cmd" );
}

