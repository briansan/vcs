##
# title: Tank.py
# by: Brian Kim
# description: a cylindrical tank that can hold liquids
#

from Cylinder import Cylinder

class Tank( Cylinder ):
  def valve( self, x=None ):
    if x == None:
      return self._valve
    else:
      if 0.0 <= x and x <= 1.0:
        self._valve = round(x,3)

  def __init__( self, radius=3, height=4, valve=0.5 ):
    Cylinder.__init__( self, radius, height )
    self._valve = valve
