#!/usr/bin/env python3

import minimalmodbus
import serial
import time
import os

baudrate = 9600 # from datasheet
parity = 'N'
bytesize = 8 # from datasheet
stopbits = 1 # from datasheet
timeout = 0.05

register = {
	'temperature': 258,
	'humidity': 259,
	'network_address_of_the_device': 4,
	'exchange_rate': 5,
	'device_response_delay': 6,
	'number_of_stopbits': 7,
	'software_version': 16
}

function = {
	'read': 3,
	'write': 6
}

decimals_number = {
	0: 0,
	1: 1,
	2: 2
}

port = '/dev/ttyUSB1' # serial port
slave_adress = 16 # 10cc

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
        self.index = HTT100.sensors_count
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

    def __del__(self):
        print('Сенсор {0} отключен'.format(self.index))
        HTT100.sensors_count -= 1

        if HTT100.sensors_count == 0:
            print('Все датчики отключены')
        else:
            print('Осталось {0:d} работающих датчиков'.format(RHTT100.sensors_count))

    def get_temperature(self):
        self.temperature = self.instrument.read_register(register['temperature'], decimals_number[2], function['read'], signed=True)
        return self.temperature

    def get_humidity(self):
        self.humidity = self.instrument.read_register(register['humidity'], decimals_number[2], function['read'])
        return self.humidity

    def get_network_address_of_the_device(self):
        self.network_address_of_the_device = self.instrument.read_register(register['network_address_of_the_device'], decimals_number[0], function['read'])
        return self.network_address_of_the_device

    def get_exchange_rate(self):
        self.exchange_rate = self.instrument.read_register(register['exchange_rate'], decimals_number[0], function['read'])
        return self.exchange_rate

    def get_device_response_delay(self):
        self.device_response_delay = self.instrument.read_register(register['device_response_delay'], decimals_number[0], function['read'])
        return self.device_response_delay

    def get_number_of_stopbits(self):
        self.number_of_stopbits = self.instrument.read_register(register['number_of_stopbits'], decimals_number[0], function['read'])
        return self.number_of_stopbits

    def get_software_version(self):
        self.software_version = self.instrument.read_register(register['software_version'], decimals_number[0], function['read'])
        return self.software_version

    def get_device_information(self):
    	print("network_address_of_the_device: " + str(self.get_network_address_of_the_device()) + "\n" 
              + "exchange_rate: "               + str(self.get_exchange_rate())                 + "\n" 
              + "device_response_delay: "       + str(self.get_device_response_delay())         + "\n"
              + "number_of_stopbits: "          + str(self.get_number_of_stopbits())            + "\n"
              + "software_version: "            + str(self.get_software_version())              + "\n")


sensor_1 = HTT100(port, slave_adress, baudrate, parity, bytesize, stopbits, timeout)
sensor_1.get_device_information()
for i in range(10):
    print()
    print("temperature = " + str(sensor_1.get_temperature()) +" C" + " humidity = " + str(sensor_1.get_humidity()) + "%")
    time.sleep(1)
del sensor_1
