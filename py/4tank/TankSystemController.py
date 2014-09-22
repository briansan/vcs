##
# title: Tank System Controller
# by: Brian Kim
# description: top level tank system controller
# 

from model import *
from interface import *

class TankSystemController( TankInfoTable.DataSource, TankInfoTable.Delegate, PumpInfoTable.DataSource, PumpInfoTable.Delegate ):

  def __init__( self, upper_tank_radius=4, lower_tank_radius=5 ):
    self.model = TankSystem( upper_tank_radius, lower_tank_radius )   
    self.interface = TankSystemInterface( self, self, self, self, self.step )

  # lifecycle methods
  def start( self ):
    self.interface.start()

  def step( self ):
    self.model.step()
    self.updateUI()

  def updateUI( self ):
    self.interface.update()

  # tank info table data source
  def tl_info( self ):
    tank = self.model.tank( TankSystem.TankIndex.tl )
    return TankInfo( tank.water_height(), tank.water_in(), tank.water_out(), tank.water_volume(), tank.capacity(), tank.valve_ratio() )

  def tr_info( self ):
    tank = self.model.tank( TankSystem.TankIndex.tr )
    return TankInfo( tank.water_height(), tank.water_in(), tank.water_out(), tank.water_volume(), tank.capacity(), tank.valve_ratio() )
    
  def bl_info( self ):
    tank = self.model.tank( TankSystem.TankIndex.bl )
    return TankInfo( tank.water_height(), tank.water_in(), tank.water_out(), tank.water_volume(), tank.capacity(), tank.valve_ratio() )

  def br_info( self ):
    tank = self.model.tank( TankSystem.TankIndex.br )
    return TankInfo( tank.water_height(), tank.water_in(), tank.water_out(), tank.water_volume(), tank.capacity(), tank.valve_ratio() )

  # tank info delegate
  def tl_valve_inc_button_clicked( self ):
    tank = self.model.tank( TankSystem.TankIndex.tl )
    tank.valve_ratio( tank.valve_ratio() + 0.1 )
    self.updateUI()

  def tl_valve_dec_button_clicked( self ):
    tank = self.model.tank( TankSystem.TankIndex.tl )
    tank.valve_ratio( tank.valve_ratio() - 0.1 )
    self.updateUI()

  def tr_valve_inc_button_clicked( self ):
    tank = self.model.tank( TankSystem.TankIndex.tr )
    tank.valve_ratio( tank.valve_ratio() + 0.1 )
    self.updateUI()

  def tr_valve_dec_button_clicked( self ):
    tank = self.model.tank( TankSystem.TankIndex.tr )
    tank.valve_ratio( tank.valve_ratio() - 0.1 )
    self.updateUI()

  def bl_valve_inc_button_clicked( self ):
    tank = self.model.tank( TankSystem.TankIndex.bl )
    tank.valve_ratio( tank.valve_ratio() + 0.1 )
    self.updateUI()

  def bl_valve_dec_button_clicked( self ):
    tank = self.model.tank( TankSystem.TankIndex.bl )
    tank.valve_ratio( tank.valve_ratio() - 0.1 )
    self.updateUI()

  def br_valve_inc_button_clicked( self ):
    tank = self.model.tank( TankSystem.TankIndex.br )
    tank.valve_ratio( tank.valve_ratio() + 0.1 )
    self.updateUI()

  def br_valve_dec_button_clicked( self ):
    tank = self.model.tank( TankSystem.TankIndex.br )
    tank.valve_ratio( tank.valve_ratio() - 0.1 )
    self.updateUI()

  # pump info table data source
  def left_info( self ):
    pump = self.model.pump( TankSystem.PumpIndex.left )
    return PumpInfo( pump.velocity(), pump.valve_ratio() )

  def right_info( self ):
    pump = self.model.pump( TankSystem.PumpIndex.right )
    return PumpInfo( pump.velocity(), pump.valve_ratio() )

  # pump info table delegate
  def left_velocity_inc_button_clicked( self ):
    pump = self.model.pump( TankSystem.PumpIndex.left )
    pump.velocity( pump.velocity() + 0.1 )
    self.updateUI()

  def left_velocity_dec_button_clicked( self ):
    pump = self.model.pump( TankSystem.PumpIndex.left )
    pump.velocity( pump.velocity() - 0.1 )
    self.updateUI()

  def left_valve_inc_button_clicked( self ):
    pump = self.model.pump( TankSystem.PumpIndex.left )
    pump.valve_ratio( pump.valve_ratio() + 0.1 )
    self.updateUI()

  def left_valve_dec_button_clicked( self ):
    pump = self.model.pump( TankSystem.PumpIndex.left )
    pump.valve_ratio( pump.valve_ratio() - 0.1 )
    self.updateUI()

  def right_velocity_inc_button_clicked( self ):
    pump = self.model.pump( TankSystem.PumpIndex.right )
    pump.velocity( pump.velocity() + 0.1 )
    self.updateUI()

  def right_velocity_dec_button_clicked( self ):
    pump = self.model.pump( TankSystem.PumpIndex.right )
    pump.velocity( pump.velocity() - 0.1 )
    self.updateUI()

  def right_valve_inc_button_clicked( self ):
    pump = self.model.pump( TankSystem.PumpIndex.right )
    pump.valve_ratio( pump.valve_ratio() + 0.1 )
    self.updateUI()

  def right_valve_dec_button_clicked( self ):
    pump = self.model.pump( TankSystem.PumpIndex.right )
    pump.valve_ratio( pump.valve_ratio() - 0.1 )
    self.updateUI()
