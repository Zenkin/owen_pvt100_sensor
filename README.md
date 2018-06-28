# owen_pvt100_sensor

For Airalab, https://aira.life 06-2018

## Dependencies  
It is the only dependency two dependencies:   
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
    
## Описание 

### Параметры

Дефолтные параметры, прописанные в launch файле:

    /thc_sensor/baudrate: 9600   
    /thc_sensor/port: /dev/ttyUSB1   
    /thc_sensor/publication_period: 1   
    /thc_sensor/slave_adress: 16   
    /thc_sensor/timeout: 0.05   
 
Замечания:
* Парметр timeout (Максимальное время захвата интерфейса шины) нельзя ставить меньше 0.05 секунды
* При установлении параметра publication_period равным 0, периодический опрос проводиться не будет

### Сервисы

    get_humidity       
*Тип сообщения:* sensor/humidity_service     
*Принимаемые аргументы:* нет   
*Описание:* возвращает значение влажности (float64), а также Header   

    get_temperature       
*Тип сообщения:* sensor/temperature_service    
*Принимаемые аргументы:* нет   
*Описание:* возвращает значение температуры (float64), а также Header   

    update_parameters      
*Тип сообщения:* sensor/update_service     
*Принимаемые аргументы:* нет  
*Описание:* обновляет и применяет параметры, которые были записаны через rosparam set    

### Topics 

    /thc_driver/humidity  
*Тип:* sensor/humidity   
*Описание:* публикует данные о влажности (float64), а также Header

    /thc_driver/temperature   
*Тип:* sensor/temperature    
*Описание:* публикует данные о температуре (float64), а также Header   
