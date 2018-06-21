#!/usr/bin/env python3

import minimalmodbus
import serial
import serial.rs485

port = '/dev/ttyUSB0' # serial port
slave_adress = 16 # 10cc
## Number of the first register 0x0102 16cc or 258 10cc ##
hex_number = 102
dec_number = 258
dec_name_number = 1
register_number = dec_name_number
number_of_decimals = 2 # temperature value from -4000 to +12000 C
baudrate = 57600 # from datasheet
bytesize = 8 # from datasheet
stopbits = 1 # from datasheet
timeout = 0.1 # where to get it from?

def main():
    print("starting...")

    minimalmodbus.BAUDRATE = baudrate
    minimalmodbus.TIMEOUT = timeout
    instrument = minimalmodbus.Instrument(port, slave_adress, mode='rtu')
    instrument.mode = 'rtu' # rtu or ascii mode
    instrument.serial.rs485_mode = serial.rs485.RS485Settings()
    print(instrument.read_register(register_number, numberOfDecimals=2, functioncode=3, signed=True)) # Registernumber, number of decimals
    instrument.debug = True     

main()