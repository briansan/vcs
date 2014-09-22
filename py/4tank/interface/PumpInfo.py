##
# title: PumpInfo.py
# by: Brian Kim
# description: a class that defines the information that can be produced from
#   a pump
#

class PumpInfo():
  def __init__ ( self, velocity=1, valve_ratio=0.5 ):
    self.velocity = velocity
    self.valve_ratio = valve_ratio
