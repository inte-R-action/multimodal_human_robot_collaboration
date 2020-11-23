cmake_minimum_required(VERSION 3.5)
project(sam_custom_messages)
set(CMAKE_VERBOSE_MAKEFILE ON)
# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()
# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
# For Windows, MSVC compiler disable boost autolinking
add_definitions( -DBOOST_ALL_NO_LIB )
# And force all boost libraries to link dynamically
add_definitions( -DBOOST_ALL_DYN_LINK )
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  message_generation
  diagnostic_msgs
  geometry_msgs
  sensor_msgs
  std_msgs
)
## System dependencies are found with CMake''s conventions
################################################
## Declare ROS messages, services and actions ##
################################################
add_message_files(
    FILES
    Object.msg
    capability.msg
    current_action.msg
    diagnostics.msg
    hand_pos.msg
    object_state.msg
    robot_state.msg
    user_prediction.msg
)
find_package( diagnostic_msgs REQUIRED)
find_package( geometry_msgs REQUIRED)
find_package( roscpp REQUIRED)
find_package( sensor_msgs REQUIRED)
find_package( std_msgs REQUIRED)
## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
  diagnostic_msgs
  geometry_msgs
  sensor_msgs
  std_msgs
)
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
  CATKIN_DEPENDS
  "message_runtime"
  "diagnostic_msgs"
  "geometry_msgs"
  "roscpp"
  "sensor_msgs"
  "std_msgs"
)
###########
## Build ##
###########
## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  include
  ${PROJECT_SOURCE_DIR}
  ${Boost_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
  "C:/Program Files/MATLAB/R2020b/extern/include"
  "C:/Program Files/MATLAB/R2020b/extern/include/MatlabDataArray"
  "C:/Program Files/MATLAB/R2020b/toolbox/ros/include/ros1"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/include"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/console_bridge/include"
  "C:/Program Files/MATLAB/R2020b/toolbox/ros/mlroscpp/custom_messages/include"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/boost/include/boost-1_70"
  "include/sam_custom_messages"
)
set (CMAKE_SKIP_BUILD_RPATH false)
set (CMAKE_BUILD_WITH_INSTALL_RPATH true)
set (CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
## Get list of .c files in project source directory
file(GLOB ${PROJECT_NAME}_C_SOURCES RELATIVE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/*.c)
## Get list of .cpp files in project source directory
file(GLOB ${PROJECT_NAME}_CPP_SOURCES RELATIVE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/*.cpp)
## Specify library folders
link_directories("C:/Program Files/MATLAB/R2020b/extern/lib/win64/microsoft")
## Specify library folders
link_directories("C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/console_bridge/lib")
## Specify library folders
link_directories("C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/lib")
## Specify library folders
link_directories("C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/boost/lib")
# Declare library
add_library(
    sam_custom_messages_matlab 
    SHARED
    src/sam_custom_messages_Object_common.cpp
    src/sam_custom_messages_msg_Object_publisher.cpp
    src/sam_custom_messages_msg_Object_subscriber.cpp
    src/sam_custom_messages_capability_common.cpp
    src/sam_custom_messages_msg_capability_publisher.cpp
    src/sam_custom_messages_msg_capability_subscriber.cpp
    src/sam_custom_messages_current_action_common.cpp
    src/sam_custom_messages_msg_current_action_publisher.cpp
    src/sam_custom_messages_msg_current_action_subscriber.cpp
    src/sam_custom_messages_diagnostics_common.cpp
    src/sam_custom_messages_msg_diagnostics_publisher.cpp
    src/sam_custom_messages_msg_diagnostics_subscriber.cpp
    src/sam_custom_messages_hand_pos_common.cpp
    src/sam_custom_messages_msg_hand_pos_publisher.cpp
    src/sam_custom_messages_msg_hand_pos_subscriber.cpp
    src/sam_custom_messages_object_state_common.cpp
    src/sam_custom_messages_msg_object_state_publisher.cpp
    src/sam_custom_messages_msg_object_state_subscriber.cpp
    src/sam_custom_messages_robot_state_common.cpp
    src/sam_custom_messages_msg_robot_state_publisher.cpp
    src/sam_custom_messages_msg_robot_state_subscriber.cpp
    src/sam_custom_messages_user_prediction_common.cpp
    src/sam_custom_messages_msg_user_prediction_publisher.cpp
    src/sam_custom_messages_msg_user_prediction_subscriber.cpp
)
target_include_directories(sam_custom_messages_matlab PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_link_libraries( sam_custom_messages_matlab
	"libMatlabDataArray"
	"C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/console_bridge/lib/console_bridge.lib"
	"C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/lib/class_loader.lib"
	"C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/lib/rosconsole.lib"
	"C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/lib/roscpp.lib"
	"C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/lib/roscpp_serialization.lib"
	"C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/lib/rostime.lib"
	${Boost_LIBRARIES}
	${CMAKE_DL_LIBS}
	)
## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
add_dependencies(
  sam_custom_messages_matlab
  ${${PROJECT_NAME}_EXPORTED_TARGETS}
  ${catkin_EXPORTED_TARGETS}
)
# Causes the visibility macros to use dllexport rather than dllimport,
# which is appropriate when building the dll but not consuming it.
target_compile_definitions(sam_custom_messages_matlab PRIVATE "SAM_CUSTOM_MESSAGES_BUILDING_LIBRARY")
install(
  DIRECTORY include/
  DESTINATION include
)
install(
  TARGETS sam_custom_messages_matlab
  EXPORT export_${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)
install (DIRECTORY m/ DESTINATION m/ FILES_MATCHING PATTERN "*.m")
# Generated 16-Nov-2020 14:49:33
# Copyright 2019-2020 The MathWorks, Inc.
