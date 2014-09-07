//
// title = SimpleTankNetwork.ned
// by = Brian Kim
// description = network description of uncontrolled 4tank system
//

simple OMNeTTankSlave
{
  parameters:

    // top-left 
    double tl_tank_radius  @prompt( "top-left tank radius") = default( 3.192 );
    double tl_tank_height  @prompt( "top-left tank height") = default( 5.0 );
    double tl_drain_radius @prompt( "top-left drain radius") = default( 1.0 );
    double tl_drain_height @prompt( "top-left drain height") = default( 0.5 );
    double tl_water_volume @prompt( "top-left initial water_volume") = default( 35 );

    // top-right
    double tr_tank_radius  @prompt( "top-right tank radius") = default( 3.192 );
    double tr_tank_height  @prompt( "top-right tank height") = default( 5.0 );
    double tr_drain_radius @prompt( "top-right drain radius") = default( 1.0 );
    double tr_drain_height @prompt( "top-right drain height") = default( 0.5 );
    double tr_water_volume @prompt( "top-right initial water_volume") = default( 35 );

    // bottom-left 
    double bl_tank_radius  @prompt( "bottom-left tank radius") = default( 2.985 );
    double bl_tank_height  @prompt( "bottom-left tank height") = default( 5.0 );
    double bl_drain_radius @prompt( "bottom-left drain radius") = default( 1.0 );
    double bl_drain_height @prompt( "bottom-left drain height") = default( 0.5 );
    double bl_water_volume @prompt( "bottom-left initial water_volume") = default( 35 );

    // bottom-right
    double br_tank_radius  @prompt( "bottom-right tank radius") = default( 2.985 );
    double br_tank_height  @prompt( "bottom-right tank height") = default( 5.0 );
    double br_drain_radius @prompt( "bottom-right drain radius") = default( 1.0 );
    double br_drain_height @prompt( "bottom-right drain height") = default( 0.5 );
    double br_water_volume @prompt( "bottom-right initial water_volume") = default( 35 );

    // left pump
    double left_pump_radius @prompt( "left pump radius" ) = default( 0.838 );
    double left_velocity    @prompt( "left velocity" ) = default( 2.5 );
    double left_valve_ratio @prompt( "left valve ratio" ) = default( 0.333 );

    // right pump
    double right_pump_radius @prompt( "right pump radius" ) = default( 0.838 );
    double right_velocity    @prompt( "right velocity" ) = default( 2.5 );
    double right_valve_ratio @prompt( "right valve ratio" ) = default( 0.333 );

  gates:
    input cmd;

    input clock_in;
    output clock_out;
}

simple OMNeTTankMaster
{
  gates:
    output cmd;
}

network SimpleTankNetwork
{
  submodules:
    slave : OMNeTTankSlave;
    master : OMNeTTankMaster;

  connections:
    master.cmd --> { delay = 100ms; } --> slave.cmd;

    slave.clock_out --> { delay = 1000ms; } --> slave.clock_in;
}
