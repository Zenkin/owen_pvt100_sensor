cmake_minimum_required(VERSION 2.8.3)

set(PROJECT sensor)

project(${PROJECT})

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

catkin_python_setup()

add_service_files(
  FILES
  temperature_service.srv
  humidity_service.srv
  update_service.srv
)

add_service_files(
  FILES
  temperature_service.srv
  humidity_service.srv
  update_service.srv
)

add_message_files(
  FILES
  temperature.msg
  humidity.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/start_node.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
