cmake_minimum_required(VERSION 2.8.3)

set(PROJECT temperature_sensor)

project(${PROJECT})

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package()

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)