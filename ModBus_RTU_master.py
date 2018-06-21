#!/usr/bin/env python3

import minimalmodbus
import serial
import serial.rs485

port = '/dev/ttyUSB0' # serial port
slave_adress = 16 # 10cc
## Number of the first register 0x0102 16cc or 258 10cc ##
hex_number = 102
dec_number = 258
dec_name_number = 2
register_number = dec_name_number
number_of_decimals = 2 # temperature value from -4000 to +12000 C
baudrate = 9600 # from datasheet
bytesize = 8 # from datasheet
stopbits = 2 # from datasheet
timeout = 0.1 # where to get it from?

def main():
    print("starting...")

    minimalmodbus.BAUDRATE = baudrate
    minimalmodbus.TIMEOUT = timeout
    instrument = minimalmodbus.Instrument(port, slave_adress, mode='rtu')
    instrument.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
    print(instrument.read_register(register_number, numberOfDecimals=2, functioncode=3, signed=True)) # Registernumber, number of decimals
    instrument.debug = True     

main()