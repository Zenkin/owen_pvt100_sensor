# owen_pvt100_sensor

For Airalab, https://aira.life 06-2018

## Dependencies  
It is the only two dependencies, you can download it from the links below:   
* [MinimalModbus](http://minimalmodbus.readthedocs.io/en/master/installation.html)    
* [PySerial](https://pypi.org/project/pyserial/)     

## Installation

    cd /home/<catkin_workspace>/srs
    catkin_create_pkg sensor
    git clone https://github.com/Zenkin/owen_pvt100_sensor.git   
    cp -r owen_pvt100_sensor/* sensor/
    rm -rf owen_pvt100_sensor/
    cd ..     
    catkin_make    
    catkin_make install
    source devel/setup.bash
    roslaunch sensor sensor.launch  
    
## Description 

### Parameters

Default parameters, which you can change at launch file:

    /thc_sensor/baudrate: 9600   
    /thc_sensor/port: /dev/ttyUSB1   
    /thc_sensor/publication_period: 1   
    /thc_sensor/slave_adress: 16   
    /thc_sensor/timeout: 0.05   
 
Note:
* timeout - maximum time to capture the bus interface. You can not set less than 0.05 seconds.
* При установлении параметра publication_period равным 0, периодический опрос проводиться не будет

### Msg API 

#### humidity

    Header header 
      # port name
      port string 
      
      # humidity sensor
      float64 humidity
      
      # Data checking. If the data is not reached it returns False otherwise True
      bool success
      
#### temperature  

    Header header 
      # port name
      string 
      
      # temperature sensor
      float64 temperature
      
      # Data checking. If the data is not reached it returns False otherwise True
      bool success

### Services API

#### get_humidity     
returns the humidity value (float64), and Header    
**sensor/humidity_service**       

    ---    
    Header header    
      string port    
      float64 humidity    
      bool success    

#### get_temperature  
returns the temperature value (float64), and Header
**sensor/temperature_service**

    ---    
    Header header   
      string port   
      float64 temperature   
      bool success  

#### update_parameters 
updates and applies parameters that have been changed through the rosparam set   
**sensor/update_service**   

    ---
    Header header
      string log

### Topics 

    /thc_driver/humidity  
*Тип:* sensor/humidity   
*Описание:* публикует данные о влажности (float64), а также Header

    /thc_driver/temperature   
*Тип:* sensor/temperature    
*Описание:* публикует данные о температуре (float64), а также Header   
