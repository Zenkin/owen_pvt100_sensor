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

    for slave_adress_test in range(247):
        instrument = minimalmodbus.Instrument(port, slave_adress_test+1)
        instrument.debug = True
        for register_number_test in [1, 2, 3]:
        	try:
                print(instrument.read_register(register_number_test, 4, 3, True)) # Registernumber, number of decimals
            except:
            	print("slave adress: " + str(slave_adress_test) + " adress: " + str(register_number_test) + " ERROR")

main()