#!/usr/bin/env python3

import minimalmodbus
import serial

port = '/dev/ttyUSB0' # serial port
slave_adress = 16 # 10cc
## Number of the first register 0x0102 16cc or 258 10cc ##
hex_number = 102
dec_number = 258
register_number = dec_number
number_of_decimals = 1 # temperature value from -4000 to +12000 C

def main():
    print("starting...")
    instrument = minimalmodbus.Instrument(port, slave_adress)
    temperature = instrument.read_register(register_number, 1) # Registernumber, number of decimals
    print(temperature)

main()