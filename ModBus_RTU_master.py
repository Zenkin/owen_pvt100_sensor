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
baudrate = 9600 # from datasheet
bytesize = 8 # from datasheet
stopbits = 1 # from datasheet
timeout = 0.05 # where to get it from?

def main():
    print("starting...")

    instrument = minimalmodbus.Instrument(port, slave_adress)
    instrument.serial.BAUDRATE = baudrate 
    #instrument.serial.BYTESIZE = bytesize
    #instrument.serial.PARITY   = serial.PARITY_NONE # from datasheet
    #instrument.serial.TIMEOUT  = timeout
    #instrument.serial.STOPBITS = stopbits

    print("INFORMATION")
    print("Serial port: " + str(port))
    print("Slave adress: " + str(slave_adress))
    print("Boudrate: " + str(instrument.serial.BAUDRATE))
    print("Bytesize: " + str(instrument.serial.BYTESIZE))
    print("Stopbits: " + str(instrument.serial.STOPBITS))
    print("Parity: " + str(instrument.serial.PARITY))
    print("Timeout: " + str(instrument.serial.TIMEOUT))

    temperature = instrument.read_register(register_number, 1) # Registernumber, number of decimals
    print(temperature)

main()