##
# title: Pump Information Table
# by: Brian Kim
# description: the class that wraps around a gtk Table
#  to display information about the pumps in the tank system
#

import pygtk
pygtk.require('2.0')
import gtk

from PumpInfo import PumpInfo

class PumpInfoTable():

  class DataSource():
    def left_info(self):
      return PumpInfo()

    def right_info(self):
      return PumpInfo()

  class Delegate():
    def left_velocity_inc_button_clicked( self ):
      pass
    def left_velocity_dec_button_clicked( self ):
      pass
    def left_valve_inc_button_clicked( self ):
      pass
    def left_valve_dec_button_clicked( self ):
      pass
    def right_velocity_inc_button_clicked( self ):
      pass
    def right_velocity_dec_button_clicked( self ):
      pass
    def right_valve_inc_button_clicked( self ):
      pass
    def right_valve_dec_button_clicked( self ):
      pass

  def __init__( self, datasource=DataSource(), delegate=Delegate() ):

    # connect the data source
    self.datasource = datasource
    self.delegate = delegate

    # create labels
    self.left_label = gtk.Label( 'left' )
    self.right_label = gtk.Label( 'right' )

    # create headers
    self.velocity_label = gtk.Label( 'velocity (cm/s)' )
    self.valve_ratio_label = gtk.Label( 'valve ratio left=(tr/bl) right=(tl/br)' )

    # create the table info cells

    # 
    # left pump controller
    #

    #
    # velocity control

    # creating the gtk element components 
    self.left_velocity_wrapper = gtk.HBox()
    self.left_velocity_inc_button = gtk.Button( '+' )
    self.left_velocity_dec_button = gtk.Button( '-' )
    self.left_velocity_label = gtk.Label( '0' )

    # hook up the control signals to the delegate method caller
    self.left_velocity_dec_button.connect( 'clicked', self.velocity_dec_button_clicked, 'l' )
    self.left_velocity_inc_button.connect( 'clicked', self.velocity_inc_button_clicked, 'l' )

    # add the components to the wrapper
    self.left_velocity_wrapper.add( self.left_velocity_dec_button )
    self.left_velocity_wrapper.add( self.left_velocity_label )
    self.left_velocity_wrapper.add( self.left_velocity_inc_button )
   
    #
    # valve control

    # creating the left valve control element components
    self.left_valve_wrapper = gtk.HBox()
    self.left_valve_inc_button = gtk.Button( '+' )
    self.left_valve_dec_button = gtk.Button( '-' )
    self.left_valve_ratio_label = gtk.Label( '0' )

    # hook up the left valve control signals to the delegate method caller
    self.left_valve_dec_button.connect( 'clicked', self.valve_dec_button_clicked, 'l' )
    self.left_valve_inc_button.connect( 'clicked', self.valve_inc_button_clicked, 'l' )

    # add the components to the wrapper
    self.left_valve_wrapper.add( self.left_valve_dec_button )
    self.left_valve_wrapper.add( self.left_valve_ratio_label )
    self.left_valve_wrapper.add( self.left_valve_inc_button )

    #
    # right controller
    # 

    #
    # velocity control

    # creating the right velocity control element components
    self.right_velocity_wrapper = gtk.HBox()
    self.right_velocity_inc_button = gtk.Button( '+' )
    self.right_velocity_dec_button = gtk.Button( '-' )
    self.right_velocity_label = gtk.Label( '0' )
    
    # hook up the control signals to the delegate method caller
    self.right_velocity_inc_button.connect( 'clicked', self.velocity_inc_button_clicked, 'r' )
    self.right_velocity_dec_button.connect( 'clicked', self.velocity_dec_button_clicked, 'r' )

    # add the components to the wrapper
    self.right_velocity_wrapper.add( self.right_velocity_dec_button )
    self.right_velocity_wrapper.add( self.right_velocity_label )
    self.right_velocity_wrapper.add( self.right_velocity_inc_button )

    # 
    # valve control

    # creating the gtk element components
    self.right_valve_wrapper = gtk.HBox()
    self.right_valve_inc_button = gtk.Button( '+' )
    self.right_valve_dec_button = gtk.Button( '-' )
    self.right_valve_ratio_label = gtk.Label( '0' )

    # hooking up the control signals to the delegate method caller
    self.right_valve_inc_button.connect( 'clicked', self.valve_inc_button_clicked, 'r' )
    self.right_valve_dec_button.connect( 'clicked', self.valve_dec_button_clicked, 'r' )

    # add the components to the wrapper
    self.right_valve_wrapper.add( self.right_valve_dec_button )
    self.right_valve_wrapper.add( self.right_valve_ratio_label )
    self.right_valve_wrapper.add( self.right_valve_inc_button )

    #
    # create the control wrapper (represented as a gtk.Table)
    self.table = gtk.Table(3, 3)

    # column headers
    self.table.attach( self.left_label, 1, 2, 0, 1 )
    self.table.attach( self.right_label, 2, 3, 0, 1 )

    # row headers
    self.table.attach( self.velocity_label, 0, 1, 1, 2 )
    self.table.attach( self.valve_ratio_label, 0, 1, 2, 3 )

    # left
    self.table.attach( self.left_velocity_wrapper, 1, 2, 1, 2 )
    self.table.attach( self.left_valve_wrapper, 1, 2, 2, 3 )

    # right
    self.table.attach( self.right_velocity_wrapper, 2, 3, 1, 2 )
    self.table.attach( self.right_valve_wrapper, 2, 3, 2, 3 )

    # update ui
    self.update()

  def update( self ):
    # updating the table
    # left
    self.left_velocity_label.set_text( '{:.4}'.format(self.datasource.left_info().velocity))
    self.left_valve_ratio_label.set_text( '{:.4}'.format(self.datasource.left_info().valve_ratio))

    # right
    self.right_velocity_label.set_text( '{:.4}'.format(self.datasource.right_info().velocity))
    self.right_valve_ratio_label.set_text( '{:.4}'.format(self.datasource.right_info().valve_ratio))

  def velocity_inc_button_clicked( self, widget, data ):
    if data == 'l':
      self.delegate.left_velocity_inc_button_clicked( )
    elif data == 'r':
      self.delegate.right_velocity_inc_button_clicked( )
    else:
      raise Exception( 'invalid data sent' ) 

  def velocity_dec_button_clicked( self, widget, data ):
    if data == 'l':
      self.delegate.left_velocity_dec_button_clicked( )
    elif data == 'r':
      self.delegate.right_velocity_dec_button_clicked( )
    else:
      raise Exception( 'invalid data sent' ) 

  def valve_inc_button_clicked( self, widget, data ):
    if data == 'l':
      self.delegate.left_valve_inc_button_clicked( )
    elif data == 'r':
      self.delegate.right_valve_inc_button_clicked( )
    else:
      raise Exception( 'invalid data sent' ) 

  def valve_dec_button_clicked( self, widget, data ):
    if data == 'l':
      self.delegate.left_valve_dec_button_clicked( )
    elif data == 'r':
      self.delegate.right_valve_dec_button_clicked( )
    else:
      raise Exception( 'invalid data sent' ) 

if __name__ == '__main__':
  tbl = PumpInfoTable()
  w = gtk.Window()
  w.add(tbl.table)
  w.show_all()
  gtk.main()

