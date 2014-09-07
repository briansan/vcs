# 
# title: 4tank Makefile
# by: Brian Kim
# description: makefile for the 4 tank system
#

CC = gcc

BIN_PATH = bin

INC_PATH = include
INC_FLAG = -I$(INC_PATH)

SRC_PATH = src

LIB_PATH = lib
LIB_FLAG = -L$(LIB_PATH) -lTank

OBJ_PATH = obj
OBJS = $(OBJ_PATH)/TankController.o $(OBJ_PATH)/TankSystem.o $(OBJ_PATH)/Types.o

# OMNeTTankSystem:	omnet/ libTank.a
#			( cd omnet && opp_makemake -I../include -L../lib -lTank -f -O../$(BIN_PATH))
#			make --directory=omnet

TankSystemTest:		libTank.a
			$(CC) $(INC_FLAG) $(LIB_FLAG) -o $(BIN_PATH)/TankSystemTest $(SRC_PATH)/TankSystemTest.cpp

TankTest:		libTank.a
			$(CC) $(INC_FLAG) $(LIB_FLAG) -o $(BIN_PATH)/TankTest -c $(SRC_PATH)/TankTest.cpp

libTank.a:		TankSystem.o TankController.o Types.o
			ar -r $(LIB_PATH)/libTank.a $(OBJS)

TankSystem.o:		$(SRC_PATH)/TankSystem.cpp 
			$(CC) $(INC_FLAG) -o $(OBJ_PATH)/TankSystem.o -c $(SRC_PATH)/TankSystem.cpp

TankController.o:	$(SRC_PATH)/TankController.cpp 
			$(CC) $(INC_FLAG) -o $(OBJ_PATH)/TankController.o -c $(SRC_PATH)/TankController.cpp

Types.o:		$(SRC_PATH)/Types.cpp $(INC_PATH)	
			$(CC) $(INC_FLAG) -o $(OBJ_PATH)/Types.o -c $(SRC_PATH)/Types.cpp

clean:			
			rm bin/* obj/* lib/*
