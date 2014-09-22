##
# title: TankInfo.py
# by: Brian Kim
# description: a class that defines the information that can be produced from
#   a tank
#

class TankInfo():
  def __init__ ( self, water_height=0.15, water_in=0, water_out=0, water_volume=15, 
                         tank_volume=100, valve_ratio=0.5 ):
    self.water_height = water_height
    self.water_in = water_in
    self.water_out = water_out
    self.water_volume = water_volume
    self.tank_volume = tank_volume
    self.valve_ratio = valve_ratio
