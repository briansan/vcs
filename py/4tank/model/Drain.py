##
# title: Drain.py
# by: Brian Kim
# description: a cylindrical drain that can dispense water
#  at a variable rate
#

from Tank import Tank

class Drain( Tank ):
 def __init__( self, radius=1.5, height=2, valve=0.5 ):
   Tank.__init__( self, radius, height, valve )
