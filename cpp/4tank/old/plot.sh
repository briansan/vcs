#!/bin/bash
#
# title = plot.sh
# by = Brian kim
# description = plotting the output of the program
#
GCC -o TankSystem TankSystem.c

#for ((i=0; i<100; ++i));
#  do
#    x=('$i/1000'|bc)
   ./TankSystem 0.8 0.8 > tmp
   tail -n 1 tmp 
#  done
