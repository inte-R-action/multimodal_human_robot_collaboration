# Install script for directory: C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
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

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages/msg" TYPE FILE FILES
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg"
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/capability.msg"
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/current_action.msg"
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/diagnostics.msg"
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/hand_pos.msg"
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/object_state.msg"
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/robot_state.msg"
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/user_prediction.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages/cmake" TYPE FILE FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messages-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/devel/include/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "C:/Users/inter/AppData/Roaming/MathWorks/MATLAB/R2020b/ros1/win64/venv/Scripts/python2.exe" -m compileall "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/devel/lib/site-packages/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/site-packages" TYPE DIRECTORY FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/devel/lib/site-packages/sam_custom_messages")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messages.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages/cmake" TYPE FILE FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messages-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages/cmake" TYPE FILE FILES
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messagesConfig.cmake"
    "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/build/sam_custom_messages/catkin_generated/installspace/sam_custom_messagesConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sam_custom_messages" TYPE FILE FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/include/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY OPTIONAL FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/devel/lib/sam_custom_messages_matlab.lib")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE SHARED_LIBRARY FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/devel/bin/sam_custom_messages_matlab.dll")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/m/" TYPE DIRECTORY FILES "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/m/" FILES_MATCHING REGEX "/[^/]*\\.m$")
endif()

