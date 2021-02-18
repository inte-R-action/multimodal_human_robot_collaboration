cmake_minimum_required(VERSION 2.8.3)
project(hri_static_demo)

add_executable(gripper_demo_test src/gripper_demo_test.cpp)
target_link_libraries(gripper_demo_test ${catkin_LIBRARIES} ${Boost_LIBRARIES})

add_executable(hri_static_demo src/hri_static_demo.cpp )
target_link_libraries(hri_static_demo ${catkin_LIBRARIES} ${Boost_LIBRARIES})

install(TARGETS ${PROJECT_NAME} DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

