# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "sam_custom_messages: 8 messages, 0 services")

set(MSG_I_FLAGS "-Isam_custom_messages:/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg;-Idiagnostic_msgs:/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(sam_custom_messages_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg" "std_msgs/Header:geometry_msgs/Pose:geometry_msgs/Point:geometry_msgs/Quaternion:sam_custom_messages/Object"
)

get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg" "diagnostic_msgs/DiagnosticStatus:std_msgs/Header:diagnostic_msgs/KeyValue"
)

get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg" "geometry_msgs/Quaternion:geometry_msgs/Point:std_msgs/Header:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg" ""
)

get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg" "std_msgs/Header:geometry_msgs/Pose:geometry_msgs/Point:geometry_msgs/Quaternion:sam_custom_messages/Object"
)

get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg" "std_msgs/Header:geometry_msgs/Pose:geometry_msgs/Point:geometry_msgs/Quaternion:sensor_msgs/JointState"
)

get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
add_custom_target(_sam_custom_messages_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sam_custom_messages" "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/DiagnosticStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/KeyValue.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/JointState.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_cpp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
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
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_cpp _sam_custom_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sam_custom_messages_gencpp)
add_dependencies(sam_custom_messages_gencpp sam_custom_messages_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sam_custom_messages_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_eus(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_eus(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/DiagnosticStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/KeyValue.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_eus(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_eus(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_eus(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_eus(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/JointState.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_eus(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
)

### Generating Services

### Generating Module File
_generate_module_eus(sam_custom_messages
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(sam_custom_messages_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(sam_custom_messages_generate_messages sam_custom_messages_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_eus _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_eus _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_eus _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_eus _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_eus _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_eus _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_eus _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_eus _sam_custom_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sam_custom_messages_geneus)
add_dependencies(sam_custom_messages_geneus sam_custom_messages_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sam_custom_messages_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_lisp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_lisp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/DiagnosticStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/KeyValue.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_lisp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_lisp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_lisp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_lisp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/JointState.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_lisp(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
)

### Generating Services

### Generating Module File
_generate_module_lisp(sam_custom_messages
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(sam_custom_messages_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(sam_custom_messages_generate_messages sam_custom_messages_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_lisp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_lisp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_lisp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_lisp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_lisp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_lisp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_lisp _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_lisp _sam_custom_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sam_custom_messages_genlisp)
add_dependencies(sam_custom_messages_genlisp sam_custom_messages_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sam_custom_messages_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_nodejs(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_nodejs(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/DiagnosticStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/KeyValue.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_nodejs(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_nodejs(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_nodejs(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_nodejs(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/JointState.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_nodejs(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
)

### Generating Services

### Generating Module File
_generate_module_nodejs(sam_custom_messages
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(sam_custom_messages_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(sam_custom_messages_generate_messages sam_custom_messages_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_nodejs _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_nodejs _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_nodejs _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_nodejs _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_nodejs _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_nodejs _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_nodejs _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_nodejs _sam_custom_messages_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sam_custom_messages_gennodejs)
add_dependencies(sam_custom_messages_gennodejs sam_custom_messages_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sam_custom_messages_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/DiagnosticStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/diagnostic_msgs/cmake/../msg/KeyValue.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/JointState.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
)
_generate_msg_py(sam_custom_messages
  "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
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
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/capability.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/current_action.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/diagnostics.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/hand_pos.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/Object.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/object_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/robot_state.msg" NAME_WE)
add_dependencies(sam_custom_messages_generate_messages_py _sam_custom_messages_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/james/multimodal_human_robot_collaboration/catkin_ws/src/sam_custom_messages/msg/user_prediction.msg" NAME_WE)
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
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(sam_custom_messages_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(sam_custom_messages_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()
if(TARGET diagnostic_msgs_generate_messages_cpp)
  add_dependencies(sam_custom_messages_generate_messages_cpp diagnostic_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sam_custom_messages
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(sam_custom_messages_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(sam_custom_messages_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(sam_custom_messages_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()
if(TARGET diagnostic_msgs_generate_messages_eus)
  add_dependencies(sam_custom_messages_generate_messages_eus diagnostic_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sam_custom_messages
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(sam_custom_messages_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(sam_custom_messages_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(sam_custom_messages_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()
if(TARGET diagnostic_msgs_generate_messages_lisp)
  add_dependencies(sam_custom_messages_generate_messages_lisp diagnostic_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sam_custom_messages
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(sam_custom_messages_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(sam_custom_messages_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(sam_custom_messages_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()
if(TARGET diagnostic_msgs_generate_messages_nodejs)
  add_dependencies(sam_custom_messages_generate_messages_nodejs diagnostic_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sam_custom_messages
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py sensor_msgs_generate_messages_py)
endif()
if(TARGET diagnostic_msgs_generate_messages_py)
  add_dependencies(sam_custom_messages_generate_messages_py diagnostic_msgs_generate_messages_py)
endif()
