cmake_minimum_required(VERSION 2.8.3)
project(gripper_control)

#find_package(catkin REQUIRED COMPONENTS
#  robotiq_2f_gripper_control
#)

add_executable(${PROJECT_NAME} src/robotiq_gripper_control.cpp)
target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES} ${Boost_LIBRARIES})
install(TARGETS ${PROJECT_NAME} DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

