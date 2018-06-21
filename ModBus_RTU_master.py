#!/usr/bin/env python3

import minimalmodbus
import serial

baudrate = 9600 # from datasheet
parity = 'N'
bytesize = 8 # from datasheet
stopbits = 1 # from datasheet
timeout = 0.05

port = '/dev/ttyUSB1' # serial port
slave_adress = 16 # 10cc
temperature_register = 258

class HTT100:

    sensors_count = 0

    def __init__(self, port, slave_adress, baudrate, parity, bytesize, stopbits, timeout):
        minimalmodbus.BAUDRATE = baudrate
        minimalmodbus.PARITY = parity
        minimalmodbus.BYTESIZE  = bytesize
        minimalmodbus.STOPBITS  = stopbits
        minimalmodbus.TIMEOUT = timeout 
        self.instrument = minimalmodbus.Instrument(port, slave_adress, mode='rtu')
        self.instrument.mode = minimalmodbus.MODE_RTU # set rtu mode
        HTT100.sensors_count += 1
        print("---------------------------")
        print("|          INFO           |")
        print("---------------------------")
        print("Port: " +str(port))
        print("Slave adress: " +str(slave_adress))
        print("Boudrate" +str(baudrate))
        print("Parity: " +str(parity))
        print("Bytesize" +str(bytesize))
        print("Stopbits: " +str(stopbits))
        print("Timeout" +str(timeout))


    def get_temperature(self):
        self.temperature = self.instrument.read_register(temperature_register, numberOfDecimals=2, functioncode=3, signed=True)
        return self.temperature

sensor_1 = HTT100(port, slave_adress, baudrate, parity, bytesize, stopbits, timeout)
print(sensor_1.get_temperature)