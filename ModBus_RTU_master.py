#!/usr/bin/env python2.7

import minimalmodbus

port = '/dev/ttyUSB0' # serial port
slave_adress = 16 # в десятичной сс
## Вот тут номер первого регистра 0x0102 16сс или 258 10сс ##
hex_number = 102
dec_number = 258
register_number = dec_number
number_of_decimals = 1 # Значения температуры -4000 до +12000 С

def main():
    instrument = minimalmodbus.Instrument(port, slave_adress)
    temperature = instrument.read_register(register_number, 1) # Registernumber, number of decimals
	print temperature