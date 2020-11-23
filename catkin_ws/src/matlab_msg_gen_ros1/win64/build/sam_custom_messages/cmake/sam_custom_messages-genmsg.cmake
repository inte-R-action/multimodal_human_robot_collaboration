# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "sam_custom_messages: 8 messages, 0 services")

set(MSG_I_FLAGS "-Isam_custom_messages:C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg;-Istd_msgs:C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg;-Idiagnostic_msgs:C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/diagnostic_msgs/cmake/../msg;-Igeometry_msgs:C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg;-Isensor_msgs:C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/sensor_msgs/cmake/../msg;-Istd_msgs:C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(sam_custom_messages_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg" ""
)

get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/current_action.msg" "std_msgs/Header"
)

get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/object_state.msg" "geometry_msgs/Quaternion:sam_custom_messages/Object:geometry_msgs/Point:std_msgs/Header:geometry_msgs/Pose"
)

get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/capability.msg" "geometry_msgs/Quaternion:sam_custom_messages/Object:geometry_msgs/Point:std_msgs/Header:geometry_msgs/Pose"
)

get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/diagnostics.msg" "diagnostic_msgs/KeyValue:std_msgs/Header:diagnostic_msgs/DiagnosticStatus"
)

get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/robot_state.msg" "geometry_msgs/Quaternion:geometry_msgs/Pose:std_msgs/Header:geometry_msgs/Point:sensor_msgs/JointState"
)

get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/hand_pos.msg" "geometry_msgs/Quaternion:geometry_msgs/Pose:std_msgs/Header:geometry_msgs/Point"
)

get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/user_prediction.msg" "std_msgs/Header"
)

#
#  langs = gencpp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/current_action.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/object_state.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Quaternion.msg;C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Point.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/capability.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Quaternion.msg;C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Point.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/diagnostics.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/diagnostic_msgs/cmake/../msg/KeyValue.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/diagnostic_msgs/cmake/../msg/DiagnosticStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/robot_state.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Quaternion.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Pose.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Point.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/sensor_msgs/cmake/../msg/JointState.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/hand_pos.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Quaternion.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Pose.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/user_prediction.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)

### Generating Services

### Generating Module File
_generate_module_cpp(sam_custom_messages
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(sam_custom_messages_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(sam_custom_messages_generate_messages sam_custom_messages_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sam_custom_messages_gencpp)
add_dependencies(sam_custom_messages_gencpp sam_custom_messages_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sam_custom_messages_generate_messages_cpp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/current_action.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/object_state.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Quaternion.msg;C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Point.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/capability.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Quaternion.msg;C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Point.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/diagnostics.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/diagnostic_msgs/cmake/../msg/KeyValue.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/diagnostic_msgs/cmake/../msg/DiagnosticStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/robot_state.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Quaternion.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Pose.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Point.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/sensor_msgs/cmake/../msg/JointState.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/hand_pos.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Quaternion.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Pose.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg;C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/user_prediction.msg"
  "${MSG_I_FLAGS}"
  "C:/Program Files/MATLAB/R2020b/sys/ros1/win64/ros1/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)

### Generating Services

### Generating Module File
_generate_module_py(sam_custom_messages
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(sam_custom_messages_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(sam_custom_messages_generate_messages sam_custom_messages_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/inter/Documents/NatNet_SDK_3.1/NatNetSDK/Industrial_SAM/matlab_msg_gen_ros1/win64/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sam_custom_messages_genpy)
add_dependencies(sam_custom_messages_genpy sam_custom_messages_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sam_custom_messages_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(sam_custom_messages_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET diagnostic_msgs_generate_messages_cpp)
  add_dependencies(sam_custom_messages_generate_messages_cpp diagnostic_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(sam_custom_messages_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(sam_custom_messages_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(sam_custom_messages_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages)
  install(CODE "execute_process(COMMAND \"C:/Users/inter/AppData/Roaming/MathWorks/MATLAB/R2020b/ros1/win64/venv/Scripts/python2.exe\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET diagnostic_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py diagnostic_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py sensor_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py std_msgs_generate_messages_py)
endif()
