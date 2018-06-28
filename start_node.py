#!/usr/bin/python2

import rospy
from std_msgs.msg import String
from temperature_sensor.msg import temperature as temperature_msg
from temperature_sensor.msg import humidity as humidity_msg
from temperature_sensor.srv import temperature_service, temperature_serviceResponse
from temperature_sensor.srv import humidity_service, humidity_serviceResponse
from temperature_sensor.srv import update_service, update_serviceResponse
import threading
from thc_driver import *

debug = True
lock = threading.Lock()

class Node:

    repeat = False
    counter = 0

    def publication_period_controll(self):
        if self.publication_period == 0:
            Node.repeat = False
        else:
            Node.repeat = True
        

    def clear_parameters(self):
        if debug:
            rospy.loginfo("Clear all parameters [Used when parameters were not set]")
        try:
            rospy.delete_param("/thc_sensor")
        except KeyError:
            if debug:
                rospy.loginfo("Nothing to clean [parameters were not set]")


    def init(self):
        rospy.init_node('sensor', anonymous=True)
        try:
            self.port = rospy.get_param("/thc_sensor/port")
            error_get_param = False
        except:
            error_get_param = True
        try:
            self.slave_adress = rospy.get_param("/thc_sensor/slave_adress")
            error_get_param = False
        except:
            error_get_param = True
        try:
            self.baudrate = rospy.get_param("/thc_sensor/baudrate")
            error_get_param = False
        except:
            error_get_param = True
        try:
            self.capture_time = rospy.get_param("/thc_sensor/timeout")
            error_get_param = False
        except:
            error_get_param = True
        try:
            self.publication_period = rospy.get_param("/thc_sensor/publication_period")
            error_get_param = False
        except:
            error_get_param = True
        if error_get_param:
            self.clear_parameters()
            if debug:
                rospy.loginfo("Can't find parameters. Set default values ...")
            self.set_default_parameters()
            self.get_parameters()
        if debug:
            self.print_loginfo()
        self.sensor = thc_driver(self.port, self.slave_adress, self.baudrate, parity, bytesize, stopbits, self.capture_time)


    def print_loginfo(self):
        rospy.loginfo("port: " + self.port)
        rospy.loginfo("slave adress: " + str(self.slave_adress))
        rospy.loginfo("baudrate: " + str(self.baudrate))
        rospy.loginfo("capture time: " + str(self.capture_time))
        rospy.loginfo("publicationp period: " + str(self.publication_period))        


    def set_default_parameters(self):
        rospy.set_param("/thc_sensor/port", "/dev/ttyUSB1")
        rospy.set_param("/thc_sensor/slave_adress", 16)
        rospy.set_param("/thc_sensor/baudrate", 9600)
        rospy.set_param("/thc_sensor/timeout", 10)
        rospy.set_param("/thc_sensor/publication_period", 30)


    def get_parameters(self):
        self.port = rospy.get_param("/thc_sensor/port")
        self.slave_adress = rospy.get_param("/thc_sensor/slave_adress")
        self.baudrate = rospy.get_param("/thc_sensor/baudrate")
        self.capture_time = rospy.get_param("/thc_sensor/timeout")
        self.publication_period = rospy.get_param("/thc_sensor/publication_period")
        self.sensor = thc_driver(self.port, self.slave_adress, self.baudrate, parity, bytesize, stopbits, self.capture_time)          


    def start_publication(self):
        temperature_message = temperature_msg()
        humidity_message = humidity_msg()
        self.publication_period_controll()
        temperature_publication = rospy.Publisher('thc_driver/temperature', temperature_msg, queue_size=10)
        humidity_publication = rospy.Publisher('thc_driver/humidity', humidity_msg, queue_size=10)
        while not rospy.is_shutdown():
            self.publication_period_controll()
            # form a message with temperature
            temperature_message.port = self.port
            temperature_message.header.stamp = rospy.Time.now()
            temperature_message.header.frame_id = "temperure_sensor"
            lock.acquire()
            temperature_value = self.get_temperature()
            lock.release()
            if temperature_value == -200:
                temperature_message.success = False
                temperature_message.temperature = 0
            else:
                temperature_message.success = True
                temperature_message.temperature = temperature_value
            # form a message with humidity
            humidity_message.port = self.port
            humidity_message.header.stamp = rospy.Time.now()
            humidity_message.header.frame_id = "humidity_sensor"
            lock.acquire()
            humidity_value = self.get_humidity()
            lock.release()
            if humidity_value == -200:
                humidity_message.success = False
                humidity_message.humidity = 0
            else:
                humidity_message.success = True
                humidity_message.humidity = humidity_value
            # publish messages with temperature and humidity
            if Node.repeat:
                temperature_publication.publish(temperature_message)
                humidity_publication.publish(humidity_message)
                Node.counter = 0
                time.sleep(self.publication_period)
            else:
                if Node.counter == 0:
                    temperature_publication.publish(temperature_message)
                    humidity_publication.publish(humidity_message)
                    Node.counter += 1
                    if debug:
                        rospy.loginfo("publication_period_controll:repeat: False")


    def get_temperature(self):
        return self.sensor.get_temperature()


    def get_humidity(self):
        return self.sensor.get_humidity()


    def temperature_service_callback(self, request):
        temperature_message_response = temperature_serviceResponse()
        lock.acquire()
        #temperature_message_response.temperature = 25
        temperature_value = self.get_temperature()
        if temperature_value == -200:
            temperature_message_response.success = False
            temperature_message_response.temperature = 0
        else:
            temperature_message_response.success = True
            temperature_message_response.temperature = temperature_value
        temperature_message_response.port = self.port
        temperature_message_response.header.stamp = rospy.Time.now()
        temperature_message_response.header.frame_id = "temperure_sensor"
        lock.release()

        return temperature_message_response


    def humidity_service_callback(self, request):
        humidity_message_response = humidity_serviceResponse()
        lock.acquire()
        #humidity_message_response.humidity = 25
        humidity_value = self.get_humidity()
        if humidity_value == -200:
            humidity_message_response.success = False
            humidity_message_response.humidity = 0
        else:
            humidity_message_response.success = True
            humidity_message_response.humidity = humidity_value
        humidity_message_response.port = self.port
        humidity_message_response.header.stamp = rospy.Time.now()
        humidity_message_response.header.frame_id = "temperure_sensor"
        lock.release()

        return humidity_message_response


    def update_service_callback(self, request):
        update_message_response = update_serviceResponse()
        lock.acquire()
        self.get_parameters()
        lock.release()
        update_message_response.header.stamp = rospy.Time.now()
        update_message_response.header.frame_id = "update_service"
        lock.acquire()
        self.sensor = thc_driver(self.port, self.slave_adress, self.baudrate, parity, bytesize, stopbits, timeout)
        lock.release()
        update_message_response.log = "Parameters have been changed successfully"

        return update_message_response


if __name__ == '__main__':
    try:
        node = Node()
    except rospy.ROSInterruptException:
        pass
    try:
        node.init()
    except rospy.ROSInterruptException:
        pass
    try:
        rospy.Service('get_temperature', temperature_service, node.temperature_service_callback)
    except:
        rospy.loginfo("Failed to start the temperature server")
    try:
        rospy.Service('get_humidity', humidity_service, node.humidity_service_callback)
    except:
        rospy.loginfo("Failed to start the humidity server")
    try:
        rospy.Service('update_parameters', update_service, node.update_service_callback)
    except:
        rospy.loginfo("Failed to start the humidity server")
    try:
        node.start_publication()
    except rospy.ROSInterruptException:
        pass
