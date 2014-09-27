##
# title: TankController.py
# by: Brian Kim
# description: a controller of the tank
#

from Tank import Tank
from Drain import Drain

# inner tank state enumeration
class TankState:
  Empty, Draining, Static, Filling, Full, Overflow = range(6)
  translator = { Empty : "Empty", Draining : "Draining", Static : "Static",
                 Filling : "Filling", Full : "Full", Overflow : "Overflow" }

class TankController():
  # 
  # accessor methods
  #
  def capacity( self ):
    return float(self._tank.volume() + self._drain.volume())

  def drain_volume( self ):
    return float(self._drain.volume())
    
  def drain_water_volume( self ):
    return float(self._drain_water_volume)

  def state( self ):
    return self._state

  def tank_volume( self ):
    return float(self._tank.volume())

  def valve_ratio( self, x=None ):
    if x == None:
      return float(self._drain.valve(x))
    else:
      self._drain.valve(x)

  def water_height( self ):
    return float(self._water_volume / self.capacity())
    
  def water_in( self, x=None ):
    if x == None:
      return float(self._water_in)
    else:
      self._water_in = x

  def water_out( self ):
    return float(self._water_out)

  def water_spill( self ):
    return self._water_spill

  def water_volume( self ):
    return float(self._water_volume)

  #
  # constructor
  # 
  def __init__( self, tank_radius=3, tank_height=5, drain_radius=1, 
                      drain_height=1, valve_ratio=0.5, water_height=0.15 ):
    # solid properties
    self._tank  =  Tank( tank_radius, tank_height, float(drain_radius)/tank_radius )
    self._drain = Drain( drain_radius, drain_height, valve_ratio )

    # fluid properties
    self._water_volume = water_height * self.capacity()
    self._drain_water_volume = 0 
    self._water_in = 0
    self._water_out = 0
    self._water_spill = 0

    # dynamic properties
    self._state = TankState.Static if self._water_volume else TankState.Empty

    # for printing
    self.ptoken = "state"

  #
  # state testing methods 
  #
  def isDraining( self ):
    return self.water_out() > self.water_in() 

  def isEmpty( self ):
    return self.water_volume() < 0.000001

  def isFilling( self ):
    return self.water_out() < self.water_in() 

  def isFull( self ):
    return self.water_volume() >= self.capacity() 

  def isOverflow( self ):
    return (self.isFull() and self.isFilling()) or (self.water_volume() > self.capacity())
  
  def isStatic( self ):
    return not self.isFull() and not self.isFilling()

  def update( self ):
    if self.isEmpty():
      self._state = TankState.Empty
    elif self.isOverflow():
      self._state = TankState.Overflow
    elif self.isFull():
      self._state = TankState.Full
    elif self.isFilling():
      self._state = TankState.Filling
    elif self.isDraining():
      self._state = TankState.Draining
    else:
      self._state = TankState.Static

  # 
  # integration method
  #
  def step( self ):
    # dummy
    drain_volume = self._drain.volume()

    # temp
    t_water_volume = self.water_volume() + self.water_in()

    # only set water volume is tank isn't full
    if not (self.state() == TankState.Full or self.state() == TankState.Overflow):
      self._water_volume = t_water_volume

    # only update water out if there is water
    if self.water_volume():
      # set water out
      drain_amt = drain_volume * self._drain.valve()
      self._water_out = drain_amt if drain_amt < self.water_volume() else self.water_volume()

      # lessen the water volume
      self._water_volume = self.water_volume() - self.water_out() 
      if self._water_volume < 0:
        self._water_volume = 0

      # make sure valves aren't < 0
      self._water_volume = self.water_volume() if self.water_volume() else 0

    # check for the tank overflowing
    if t_water_volume > self.capacity():
      self._water_spill = t_water_volume - self.capacity()
      self._water_volume = self.capacity()

    self.update()

  def println( self, what ):
    self.ptoken = what
    y = "Tank: " + what + ": " + self.__str__()
    return y

  def __str__( self ):
    y = None
    if self.ptoken == "state":
      y = TankState.translator[ self.state() ]
    elif self.ptoken == "water volume":
      y = self.water_volume()
    elif self.ptoken == "water height":
      y = self.water_height()
    elif self.ptoken == "water in":
      y = self.water_in()
    elif self.ptoken == "water out":
      y = self.water_out()
    elif self.ptoken == "valve":
      y = self.valve()
    return str(y)

from Constants import *

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument( "n", help="number of runs", default=10, action="store_true" )
  parser.add_argument( "tank_radius", help="the radius of the tank", 
                        default=DEFAULT_LARGE_TANK_RADIUS, action="store_true" )
  parser.add_argument( "tank_height", help="the height of the tank", 
                        default=DEFAULT_LARGE_TANK_HEIGHT, action="store_true" )
  parser.add_argument( "drain_radius", help="the radius of the drain", 
                        default=DEFAULT_DRAIN_RADIUS, action="store_true" )
  parser.add_argument( "drain_height", help="the height of the drain", 
                        default=DEFAULT_DRAIN_HEIGHT, action="store_true" )
  parser.add_argument( "valve_ratio", help="the tightness of the drain valve", 
                        default=DEFAULT_DRAIN_HEIGHT, action="store_true" )
  parser.add_argument( "init_water_height", help="the initial volume of water", 
                        default=DEFAULT_LARGE_TANK_RADIUS/float(2), action="store_true" )
  args = parser.parse_args()

  info = TankInfo( args.tank_radius, args.tank_height, args.drain_radius, 
                   args.drain_height, args.valve_ratio, args.init_water_height )
  tank = TankController( info )
  

