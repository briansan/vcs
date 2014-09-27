##
# title: Cylinder.py
# by: Brian Kim
# description: an object that has a tube-like structure
#

from math import pi

class Cylinder(object):
  #
  # accessor methods 
  # 
  def area( self ):
    return self._area

  def circumference( self ):
    return self._circumference

  def height( self ):
    return self._height

  def radius( self ):
    return self._radius

  def surface_area( self ):
    return self._surface_area

  def volume( self ):
    return self._volume

  #
  # constructor
  # 
  # note: these properties are computed at
  #       init time. that makes this class immutable
  #
  def __init__( self, radius=3, height=4 ):
    # 1d properties
    self._height = height
    self._radius = radius

    # 2d properties
    self._circumference = 2*pi*radius
    self._area = pi*radius*radius
    self._surface_area = self._circumference*height + 2*self._area
    
    # 3d property
    self._volume = self._area*height
    
