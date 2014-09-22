##
# title: Pump.py
# by: Brian Kim
# description: the object that distributes water into the tanks
#

class Pump():

  def area( self ):
    return float(self._area)
    
  def flow_rate( self ):
    return float(self.area() * self.velocity())

  def pipe_radius( self ):
    return float(self._pipe_radius)

  def valve_ratio( self, x=None ):
    if x == None:
      return float(self._valve_ratio)
    else:
      if 0.0 <= x and x <= 1.0:
        self._valve_ratio = round(x,3)

  def velocity( self, x=None ):
    if x == None:
      return float(self._velocity)
    else:
      if 0.0 <= x and x <= 1.0:
        self._velocity = round(x,3)

  def __init__( self, pipe_radius, velocity=0.1, valve_ratio=0.5):
    self.velocity( velocity ) 
    self._pipe_radius = pipe_radius 
    self.valve_ratio( valve_ratio )

    from math import pi
    self._area = pi * self.pipe_radius() ** 2

    
