from TankSystem import *

# creating empty info lists
tank_infos = []
pump_infos = []

print 'upper tank radius: '
upper_tank_radius = input()
print 'lower tank radius: '
lower_tank_radius = input()

# init tank system info 
t = TankSystem( upper_tank_radius, lower_tank_radius )
t.ptoken = 'state'

for i in range( 50 ):
  t.step()
  print t

