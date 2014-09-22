##
# title: Tank Information Table
# by: Brian Kim
# description: a class that wraps around a gtk Table
#  to display dynamic information about the 4 tanks
#

import pygtk
pygtk.require('2.0')
import gtk

from TankInfo import TankInfo

class TankInfoTable():

  class DataSource():
    def tl_info(self):
      return TankInfo()

    def tr_info(self):
      return TankInfo()

    def bl_info(self):
      return TankInfo()

    def br_info(self):
      return TankInfo()

  class Delegate():
    def tl_valve_inc_button_clicked(self):
      pass
    def tl_valve_dec_button_clicked(self):
      pass
    def tr_valve_inc_button_clicked(self):
      pass
    def tr_valve_dec_button_clicked(self):
      pass
    def bl_valve_inc_button_clicked(self):
      pass
    def bl_valve_dec_button_clicked(self):
      pass
    def br_valve_inc_button_clicked(self):
      pass
    def br_valve_dec_button_clicked(self):
      pass


  def __init__( self, datasource=DataSource(), delegate=Delegate() ):

    # connect the data source
    self.datasource = datasource
    self.delegate = delegate

    # create labels
    self.tl_label = gtk.Label( 'top-left' )
    self.tr_label = gtk.Label( 'top-right' )
    self.bl_label = gtk.Label( 'bottom-left' )
    self.br_label = gtk.Label( 'bottom-right' )
    # create headers
    self.water_height_label = gtk.Label( 'water height (percentage)' )
    self.water_in_label = gtk.Label( 'water in (cm3/s)' )
    self.water_out_label = gtk.Label( 'water out (cm3/s)' )
    self.water_volume_label = gtk.Label( 'water volume (cm3)' )
    self.tank_volume_label = gtk.Label( 'tank volume (cm3)' )
    self.valve_ratio_label = gtk.Label( 'valve ratio' )

    # create the table info cells
    # top left
    self.tl_water_height_label = gtk.Label( '0' )
    self.tl_water_in_label = gtk.Label( '0' )
    self.tl_water_out_label = gtk.Label( '0' )
    self.tl_water_volume_label = gtk.Label( '0' )
    self.tl_tank_volume_label = gtk.Label( '0' )

    self.tl_valve_wrapper = gtk.HBox()
    self.tl_valve_dec_button = gtk.Button( '-' )
    self.tl_valve_ratio_label = gtk.Label( '0' )
    self.tl_valve_inc_button = gtk.Button( '+' )
    self.tl_valve_dec_button.connect( 'clicked', self.valve_dec_button_clicked, 'tl' )
    self.tl_valve_inc_button.connect( 'clicked', self.valve_inc_button_clicked, 'tl' )
    self.tl_valve_wrapper.add( self.tl_valve_dec_button )
    self.tl_valve_wrapper.add( self.tl_valve_ratio_label )
    self.tl_valve_wrapper.add( self.tl_valve_inc_button )

    # top right
    self.tr_water_height_label = gtk.Label( '0' )
    self.tr_water_in_label = gtk.Label( '0' )
    self.tr_water_out_label = gtk.Label( '0' )
    self.tr_water_volume_label = gtk.Label( '0' )
    self.tr_tank_volume_label = gtk.Label( '0' )

    self.tr_valve_wrapper = gtk.HBox()
    self.tr_valve_dec_button = gtk.Button( '-' )
    self.tr_valve_ratio_label = gtk.Label( '0' )
    self.tr_valve_inc_button = gtk.Button( '+' )
    self.tr_valve_dec_button.connect( 'clicked', self.valve_dec_button_clicked, 'tr' )
    self.tr_valve_inc_button.connect( 'clicked', self.valve_inc_button_clicked, 'tr' )
    self.tr_valve_wrapper.add( self.tr_valve_dec_button )
    self.tr_valve_wrapper.add( self.tr_valve_ratio_label )
    self.tr_valve_wrapper.add( self.tr_valve_inc_button )
    self.tr_valve_dec_button = gtk.Button( '+' )

    # bottom left
    self.bl_water_height_label = gtk.Label( '0' )
    self.bl_water_in_label = gtk.Label( '0' )
    self.bl_water_out_label = gtk.Label( '0' )
    self.bl_water_volume_label = gtk.Label( '0' )
    self.bl_tank_volume_label = gtk.Label( '0' )

    self.bl_valve_wrapper = gtk.HBox()
    self.bl_valve_dec_button = gtk.Button( '-' )
    self.bl_valve_ratio_label = gtk.Label( '0' )
    self.bl_valve_inc_button = gtk.Button( '+' )
    self.bl_valve_dec_button.connect( 'clicked', self.valve_dec_button_clicked, 'bl' )
    self.bl_valve_inc_button.connect( 'clicked', self.valve_inc_button_clicked, 'bl' )
    self.bl_valve_wrapper.add( self.bl_valve_dec_button )
    self.bl_valve_wrapper.add( self.bl_valve_ratio_label )
    self.bl_valve_wrapper.add( self.bl_valve_inc_button )

    # bottom right
    self.br_water_height_label = gtk.Label( '0' )
    self.br_water_in_label = gtk.Label( '0' )
    self.br_water_out_label = gtk.Label( '0' )
    self.br_water_volume_label = gtk.Label( '0' )
    self.br_tank_volume_label = gtk.Label( '0' )

    self.br_valve_wrapper = gtk.HBox()
    self.br_valve_dec_button = gtk.Button( '-' )
    self.br_valve_ratio_label = gtk.Label( '0' )
    self.br_valve_inc_button = gtk.Button( '+' )
    self.br_valve_dec_button.connect( 'clicked', self.valve_dec_button_clicked, 'br' )
    self.br_valve_inc_button.connect( 'clicked', self.valve_inc_button_clicked, 'br' )
    self.br_valve_wrapper.add( self.br_valve_dec_button )
    self.br_valve_wrapper.add( self.br_valve_ratio_label )
    self.br_valve_wrapper.add( self.br_valve_inc_button )

    # create table
    self.table = gtk.Table(7, 5)
    self.table.set_col_spacings( 10 )

    # column headers
    self.table.attach( self.tl_label, 1, 2, 0, 1 )
    self.table.attach( self.tr_label, 2, 3, 0, 1 )
    self.table.attach( self.bl_label, 3, 4, 0, 1 )
    self.table.attach( self.br_label, 4, 5, 0, 1 )

    # row headers
    self.table.attach( self.water_height_label, 0, 1, 1, 2 )
    self.table.attach( self.water_in_label, 0, 1, 2, 3 )
    self.table.attach( self.water_out_label, 0, 1, 3, 4 )
    self.table.attach( self.water_volume_label, 0, 1, 4, 5 )
    self.table.attach( self.tank_volume_label, 0, 1, 5, 6 )
    self.table.attach( self.valve_ratio_label, 0, 1, 6, 7 )

    # top left
    self.table.attach( self.tl_water_height_label, 1, 2, 1, 2 )
    self.table.attach( self.tl_water_in_label, 1, 2, 2, 3 )
    self.table.attach( self.tl_water_out_label, 1, 2, 3, 4 )
    self.table.attach( self.tl_water_volume_label, 1, 2, 4, 5 )
    self.table.attach( self.tl_tank_volume_label, 1, 2, 5, 6 )
    self.table.attach( self.tl_valve_wrapper, 1, 2, 6, 7 )

    # top right
    self.table.attach( self.tr_water_height_label, 2, 3, 1, 2 )
    self.table.attach( self.tr_water_in_label, 2, 3, 2, 3 )
    self.table.attach( self.tr_water_out_label, 2, 3, 3, 4 )
    self.table.attach( self.tr_water_volume_label, 2, 3, 4, 5 )
    self.table.attach( self.tr_tank_volume_label, 2, 3, 5, 6 )
    self.table.attach( self.tr_valve_wrapper, 2, 3, 6, 7 )

    # bottom left
    self.table.attach( self.bl_water_height_label, 3, 4, 1, 2 )
    self.table.attach( self.bl_water_in_label, 3, 4, 2, 3 )
    self.table.attach( self.bl_water_out_label, 3, 4, 3, 4 )
    self.table.attach( self.bl_water_volume_label, 3, 4, 4, 5 )
    self.table.attach( self.bl_tank_volume_label, 3, 4, 5, 6 )
    self.table.attach( self.bl_valve_wrapper, 3, 4, 6, 7 )

    # bottom right
    self.table.attach( self.br_water_height_label, 4, 5, 1, 2 )
    self.table.attach( self.br_water_in_label, 4, 5, 2, 3 )
    self.table.attach( self.br_water_out_label, 4, 5, 3, 4 )
    self.table.attach( self.br_water_volume_label, 4, 5, 4, 5 )
    self.table.attach( self.br_tank_volume_label, 4, 5, 5, 6 )
    self.table.attach( self.br_valve_wrapper, 4, 5, 6, 7 )

    # update ui
    self.update()

  def update( self ):
    # updating the table
    # top left
    self.tl_water_height_label.set_text( '{:.4}%'.format(self.datasource.tl_info().water_height*100))
    self.tl_water_in_label.set_text( '{:.4}'.format(self.datasource.tl_info().water_in))
    self.tl_water_out_label.set_text( '{:.4}'.format(self.datasource.tl_info().water_out))
    self.tl_water_volume_label.set_text( '{:.4}'.format(self.datasource.tl_info().water_volume))
    self.tl_tank_volume_label.set_text( '{:.4}'.format(self.datasource.tl_info().tank_volume))
    self.tl_valve_ratio_label.set_text( '{:.4}'.format(self.datasource.tl_info().valve_ratio))
    # top right
    self.tr_water_height_label.set_text( '{:.4}%'.format(self.datasource.tr_info().water_height*100))
    self.tr_water_in_label.set_text( '{:.4}'.format(self.datasource.tr_info().water_in))
    self.tr_water_out_label.set_text( '{:.4}'.format(self.datasource.tr_info().water_out))
    self.tr_water_volume_label.set_text( '{:.4}'.format(self.datasource.tr_info().water_volume))
    self.tr_tank_volume_label.set_text( '{:.4}'.format(self.datasource.tr_info().tank_volume))
    self.tr_valve_ratio_label.set_text( '{:.4}'.format(self.datasource.tr_info().valve_ratio))
    # bottom left
    self.bl_water_height_label.set_text( '{:.4}%'.format(self.datasource.bl_info().water_height*100))
    self.bl_water_in_label.set_text( '{:.4}'.format(self.datasource.bl_info().water_in))
    self.bl_water_out_label.set_text( '{:.4}'.format(self.datasource.bl_info().water_out))
    self.bl_water_volume_label.set_text( '{:.4}'.format(self.datasource.bl_info().water_volume))
    self.bl_tank_volume_label.set_text( '{:.4}'.format(self.datasource.bl_info().tank_volume))
    self.bl_valve_ratio_label.set_text( '{:.4}'.format(self.datasource.bl_info().valve_ratio))
    # bottom right
    self.br_water_height_label.set_text( '{:.4}%'.format(self.datasource.br_info().water_height*100))
    self.br_water_in_label.set_text( '{:.4}'.format(self.datasource.br_info().water_in))
    self.br_water_out_label.set_text( '{:.4}'.format(self.datasource.br_info().water_out))
    self.br_water_volume_label.set_text( '{:.4}'.format(self.datasource.br_info().water_volume))
    self.br_tank_volume_label.set_text( '{:.4}'.format(self.datasource.br_info().tank_volume))
    self.br_valve_ratio_label.set_text( '{:.4}'.format(self.datasource.br_info().valve_ratio))
    
  def valve_dec_button_clicked( self, widget, data ):
    if data == 'tl':
      self.delegate.tl_valve_dec_button_clicked( )
    elif data == 'tr':
      self.delegate.tr_valve_dec_button_clicked( )
    elif data == 'bl':
      self.delegate.bl_valve_dec_button_clicked( )
    elif data == 'br':
      self.delegate.br_valve_dec_button_clicked( )

  def valve_inc_button_clicked( self, widget, data ):
    if data == 'tl':
      self.delegate.tl_valve_inc_button_clicked( )
    elif data == 'tr':
      self.delegate.tr_valve_inc_button_clicked( )
    elif data == 'bl':
      self.delegate.bl_valve_inc_button_clicked( )
    elif data == 'br':
      self.delegate.br_valve_inc_button_clicked( )

if __name__ == '__main__':
  tbl = TankInfoTable()
  w = gtk.Window()
  w.add( tbl.table )
  w.show_all()
  gtk.main()
