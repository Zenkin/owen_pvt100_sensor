#!/usr/bin/env python3

import minimalmodbus
import serial

port = '/dev/ttyUSB0' # serial port
slave_adress = 1 # 10cc
## Number of the first register 0x0102 16cc or 258 10cc ##
hex_number = 102
dec_number = 258
register_number = dec_number
number_of_decimals = 1 # temperature value from -4000 to +12000 C
baudrate = 9600 # from datasheet
bytesize = 8 # from datasheet
stopbits = 1 # from datasheet
timeout = 0.1 # where to get it from?

def main():
    print("starting...")

    minimalmodbus.BAUDRATE = baudrate
    minimalmodbus.TIMEOUT = timeout

    #for i in range(4):
    #    instrument = minimalmodbus.Instrument(port, i+1)
    #    instrument.debug = True
    #    for j in [1, 2, 3]:
    #        print("slave_adress: " + str(i+1) + " adress: " + str(j))
    #        print(instrument.read_register(j, 4, 3, True)) # Registernumber, number of decimals
    try:
        instrument = minimalmodbus.Instrument(port, i+1)
    except IOError:
    	print("ошибка")
    #print(instrument.read_register(1, 4, 3, True))

main()