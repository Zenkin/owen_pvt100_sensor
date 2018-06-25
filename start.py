#!/usr/bin/python2 

import rospy
from std_msgs.msg import String
from HTT100 import *
debug = True

class Node:

    def clear_parameters(self):
        try:
            rospy.delete_param("/temperature_sensor")
        except KeyError:
            if debug:
                print "/temperature_sensor not set"


    def init(self):
        rospy.init_node('sensor', anonymous=True)
        try:
            self.port = rospy.get_param("/temperature_sensor/port")
            self.slave_adress = rospy.get_param("/temperature_sensor/slave_adress")
            self.baudrate = rospy.get_param("/temperature_sensor/baudrate")
            self.capture_time = rospy.get_param("/temperature_sensor/capture_time")
            self.publication_period = rospy.get_param("/temperature_sensor/publication_period")
        except:
            # Default values of serial port
            rospy.loginfo("Launch from 'rosrun'")
            rospy.loginfo("Use default parameters of serial port \n")
            self.port = '/dev/ttyUSB0'
            self.slave_adress = 16
            self.baudrate = 9600 
            self.capture_time = 10
            self.publication_period = 30
    
        if debug:
            rospy.loginfo("port: " + self.port)
            rospy.loginfo("slave adress: " + str(self.slave_adress))
            rospy.loginfo("baudrate: " + str(self.baudrate))
            rospy.loginfo("capture time: " + str(self.capture_time))
            rospy.loginfo("publicationp period: " + str(self.publication_period))

        #self.sensor = HTT100(port, slave_adress, baudrate, parity, bytesize, stopbits, timeout)

        self.sensor = '5'


    def start_publication(self):
        pub = rospy.Publisher('HTT100/temperature', String, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            pub.publish(self.get_temperature())
            rate.sleep()


    def get_temperature(self):
        #return self.sensor.get_temperature()
        return self.sensor


    def get_humidity(self):
        pass
        #return self.sensor.get_humidity()
        

if __name__ == '__main__':
    node = Node()
    node.init()
    node.start_publication()