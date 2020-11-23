# Install script for directory: /home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/james/multimodal_human_robot_collaboration/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages/msg" TYPE FILE FILES
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg"
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg"
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg"
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg"
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg"
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg"
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages/cmake" TYPE FILE FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messages-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/devel/include/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/devel/share/roseus/ros/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/devel/share/common-lisp/ros/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/devel/share/gennodejs/ros/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/james/multimodal_human_robot_collaboration/catkin_ws/devel/lib/python3/dist-packages/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/devel/lib/python3/dist-packages/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messages.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages/cmake" TYPE FILE FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messages-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages/cmake" TYPE FILE FILES
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messagesConfig.cmake"
    "/home/james/multimodal_human_robot_collaboration/catkin_ws/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messagesConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages" TYPE FILE FILES "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/package.xml")
endif()

