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
        #minimalmodbus.BAUDRATE = baudrate
        #minimalmodbus.PARITY = parity
        #minimalmodbus.BYTESIZE  = bytesize
        #minimalmodbus.STOPBITS  = stopbits
        #minimalmodbus.TIMEOUT = timeout 
        #self.instrument = minimalmodbus.Instrument(port, slave_adress, mode='rtu')
        #self.instrument.mode = minimalmodbus.MODE_RTU # set rtu mode
        HTT100.sensors_count += 1
        print("    ---------------------------")
        print("    |      SENSOR "+str(HTT100.sensors_count)+"   INFO    |")
        print("    ---------------------------")
        print(("  "), ("Port: ").ljust(20), str(port).ljust(40))
        print(("  "), ("Slave adress: ").ljust(20), str(slave_adress).ljust(40))
        print(("  "), ("Boudrate: ").ljust(20), str(baudrate).ljust(40))
        print(("  "), ("Parity: ").ljust(20), str(parity).ljust(40))
        print(("  "), ("Bytesize: ").ljust(20), str(bytesize).ljust(40))
        print(("  "), ("Stopbits: ").ljust(20), str(stopbits).ljust(40))
        print(("  "), ("Timeout: ").ljust(20), str(timeout).ljust(40))
        print("")

    def get_temperature(self):
        self.temperature = self.instrument.read_register(temperature_register, numberOfDecimals=2, functioncode=3, signed=True)
        return self.temperature

sensor_1 = HTT100(port, slave_adress, baudrate, parity, bytesize, stopbits, timeout)
for i in range(10):
    print("temperature = "sensor_1.get_temperature() +" C")
    delay(1)