# RS485_serial_communications

## Установка

    cd /home/<catkin_workspace>/srs
    catkin_create_pkg sensor
    git clone https://github.com/Zenkin/RS485_serial_communications.git   
    cp -r RS485_serial_communications/* sensor/
    rm -rf RS485_serial_communications/
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

# Полезные ссылки
[MinimalModBus](http://minimalmodbus.readthedocs.io/en/master/  "Ссылка")    
[PySerial](https://pyserial.readthedocs.io/en/latest/shortintro.html "Ссылка")     
