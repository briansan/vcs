##
# title: TankSystem.py
# by: Brian Kim
# description: a system of four tank controllers
#

from TankController import *
from Pump import *

class TankSystem():

  class TankIndex():
    tl, tr, bl, br = range(4)

  class PumpIndex():
    left, right = range(2)

  def __init__( self, upper_tank_radius, lower_tank_radius, tank_height=5,
                      drain_radius=1, drain_height=2,
                      tank_valve_ratio=0.5, init_water_height=0.15,
                      pump_pipe_radius=3, pump_velocity=0.1, pump_valve_ratio=0.5, clock=0 ):

    self._clk = clock
    self._tl = TankController( upper_tank_radius, tank_height, drain_radius, drain_height, 
                                        tank_valve_ratio, init_water_height )
    self._tr = TankController( upper_tank_radius, tank_height, drain_radius, drain_height, 
                                        tank_valve_ratio, init_water_height )
    self._bl = TankController( lower_tank_radius, tank_height, drain_radius, drain_height,
                                        tank_valve_ratio, init_water_height )
    self._br = TankController( lower_tank_radius, tank_height, drain_radius, drain_height,
                                        tank_valve_ratio, init_water_height ) 
    self._left = Pump( pump_pipe_radius, pump_velocity, pump_valve_ratio )
    self._right = Pump( pump_pipe_radius, pump_velocity, pump_valve_ratio )

    self.ptoken = 'water height'

  def __str__( self ):
    y = 'time: ' + str(self._clk) + '\n'
    y += 'TopLeft' + self._tl.println( self.ptoken )  + '\n'
    y += 'TopRight' + self._tr.println( self.ptoken )  + '\n'
    y += 'BottomLeft' + self._bl.println( self.ptoken )  + '\n'
    y += 'BottomRight' + self._br.println( self.ptoken )  + '\n'
    return y

  def clock( self ):
    return self._clk
    
  def tank( self, index ):
    y = None
    if index == TankSystem.TankIndex.tl:
      y = self._tl
    elif index == TankSystem.TankIndex.tr:
      y = self._tr
    elif index == TankSystem.TankIndex.bl:
      y = self._bl
    elif index == TankSystem.TankIndex.br:
      y = self._br
    return y

  def pump( self, index ):
    y = None
    if index == TankSystem.PumpIndex.left:
      y = self._left
    elif index == TankSystem.PumpIndex.right:
      y = self._right
    return y
  
  def step( self ):

    # dummy vars
    tl = self._tl
    tr = self._tr
    bl = self._bl
    br = self._br
    left = self._left
    right = self._right

    left_rate = left.flow_rate()
    left_ratio = left.valve_ratio()
    right_rate = right.flow_rate()
    right_ratio = right.valve_ratio()

    # top tank flow rates
    tl_flow = right_rate * right_ratio
    tr_flow = left_rate * left_ratio

    # setting top tank water in flow rates
    tl.water_in( tl_flow )
    tr.water_in( tr_flow )

    # stepping the top tanks
    tl.step()
    tr.step()

    # bottom tank flow rates
    bl_flow = tl.water_out() + left_rate * (1.0 - left_ratio)
    br_flow = tr.water_out() + right_rate * (1.0 - right_ratio)

    # set the flow rates of bottom tanks
    bl.water_in( bl_flow )
    br.water_in( br_flow )

    # step the bottom tanks
    bl.step()
    br.step()

    # increment the clock
    self._clk = self.clock() + 1

