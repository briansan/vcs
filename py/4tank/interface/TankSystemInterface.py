import pygtk
pygtk.require('2.0')
import gtk

from TankInfoTable import *
from PumpInfoTable import *

class TankSystemInterface():
  def __init__( self, tank_datasource=TankInfoTable.DataSource(), pump_datasource=PumpInfoTable.DataSource(), 
                      tank_delegate=TankInfoTable.Delegate(), pump_delegate=PumpInfoTable.Delegate(), callback=None ):

    self.window = gtk.Window()
    self.window.connect( 'delete-event', gtk.main_quit )

    self.wrapper = gtk.VBox()

    self.title_label = gtk.Label( 'Tank System:' )
    self.tanks_label = gtk.Label( 'Tanks:' )
    self.pumps_label = gtk.Label( 'Pumps:' )

    self.tank_table = TankInfoTable( tank_datasource, tank_delegate )
    self.pump_table = PumpInfoTable( pump_datasource, pump_delegate )
    
    self.step_button = gtk.Button( 'step' )
    self.step_button.connect( 'clicked', self.step_button_clicked )
    self.callback = callback

    self.window.add( self.wrapper )
    self.wrapper.add( self.title_label )
    self.wrapper.add( self.tanks_label )
    self.wrapper.add( self.tank_table.table )
    self.wrapper.add( self.pumps_label )
    self.wrapper.add( self.pump_table.table )
    self.wrapper.add( self.step_button )

  def start( self ):
    self.window.show_all()
    gtk.main()

  def update( self ):
    self.tank_table.update()
    self.pump_table.update()

  def step_button_clicked( self, widget ):
    self.callback()
