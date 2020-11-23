// Copyright 2019-2020 The MathWorks, Inc.
// Common copy functions for sam_custom_messages/robot_state
#include "boost/date_time.hpp"
#include "boost/shared_array.hpp"
#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4244)
#pragma warning(disable : 4265)
#pragma warning(disable : 4458)
#pragma warning(disable : 4100)
#pragma warning(disable : 4127)
#pragma warning(disable : 4267)
#else
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wpedantic"
#pragma GCC diagnostic ignored "-Wunused-local-typedefs"
#pragma GCC diagnostic ignored "-Wredundant-decls"
#pragma GCC diagnostic ignored "-Wnon-virtual-dtor"
#pragma GCC diagnostic ignored "-Wdelete-non-virtual-dtor"
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-variable"
#pragma GCC diagnostic ignored "-Wshadow"
#endif //_MSC_VER
#include "ros/ros.h"
#include "sam_custom_messages/robot_state.h"
#include "visibility_control.h"
#ifndef FOUNDATION_MATLABDATA_API
#include "MDArray.hpp"
#include "StructArray.hpp"
#include "TypedArrayRef.hpp"
#include "Struct.hpp"
#include "ArrayFactory.hpp"
#include "StructRef.hpp"
#include "Reference.hpp"
#endif
#ifndef FOUNDATION_MATLABDATA_API
typedef matlab::data::Array MDArray_T;
typedef matlab::data::ArrayFactory MDFactory_T;
#else
typedef foundation::matlabdata::Array MDArray_T;
typedef foundation::matlabdata::standalone::ClientArrayFactory MDFactory_T;
#endif
namespace sam_custom_messages {
namespace matlabhelper {
namespace robot_state {
  void copy_from_arr_std_msgs_Header(std_msgs::Header& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_std_msgs_Header(MDFactory_T& factory, const sam_custom_messages::robot_state::_header_type& val);
  void copy_from_arr_ros_Time(ros::Time& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_ros_Time(MDFactory_T& factory, const std_msgs::Header::_stamp_type& val);
  void copy_from_arr_sensor_msgs_JointState(sensor_msgs::JointState& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_sensor_msgs_JointState(MDFactory_T& factory, const sam_custom_messages::robot_state::_jointstate_type& val);
  void copy_from_arr_geometry_msgs_Pose(geometry_msgs::Pose& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_geometry_msgs_Pose(MDFactory_T& factory, const sam_custom_messages::robot_state::_pose_type& val);
  void copy_from_arr_geometry_msgs_Point(geometry_msgs::Point& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_geometry_msgs_Point(MDFactory_T& factory, const geometry_msgs::Pose::_position_type& val);
  void copy_from_arr_geometry_msgs_Quaternion(geometry_msgs::Quaternion& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_geometry_msgs_Quaternion(MDFactory_T& factory, const geometry_msgs::Pose::_orientation_type& val);
  //----------------------------------------------------------------------------
  void copy_from_arr_std_msgs_Header(std_msgs::Header& val, const matlab::data::StructArray& arr) {
    // _std_msgs_Header.seq
    try {
        const matlab::data::TypedArray<uint32_t> _headerseq_arr = arr[0]["seq"];
        val.seq = _headerseq_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'seq' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'seq' is wrong type; expected a uint32.");
    }
    // _std_msgs_Header.stamp
    try {
        const matlab::data::StructArray _headerstamp_arr = arr[0]["stamp"];
        copy_from_arr_ros_Time(val.stamp,_headerstamp_arr);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'stamp' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'stamp' is wrong type; expected a struct.");
    }
    // _std_msgs_Header.frame_id
    try {
        const matlab::data::CharArray _headerframe_id_arr = arr[0]["frame_id"];
        val.frame_id = _headerframe_id_arr.toAscii();
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'frame_id' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'frame_id' is wrong type; expected a string.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T get_arr_std_msgs_Header(MDFactory_T& factory, const sam_custom_messages::robot_state::_header_type& val) {
    auto _headeroutArray = factory.createStructArray({1,1},{"seq","stamp","frame_id"});
    // _std_msgs_Header.seq
    _headeroutArray[0]["seq"] = factory.createScalar(val.seq);
    // _std_msgs_Header.stamp
    _headeroutArray[0]["stamp"] = get_arr_ros_Time(factory, val.stamp);
    // _std_msgs_Header.frame_id
    _headeroutArray[0]["frame_id"] = factory.createCharArray(val.frame_id);
    return std::move(_headeroutArray);
  }
  //----------------------------------------------------------------------------
  void copy_from_arr_ros_Time(ros::Time& val, const matlab::data::StructArray& arr) {
    // _ros_Time.sec
    try {
        const matlab::data::TypedArray<uint32_t> _header_stampsec_arr = arr[0]["sec"];
        val.sec = _header_stampsec_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'sec' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'sec' is wrong type; expected a uint32.");
    }
    // _ros_Time.nsec
    try {
        const matlab::data::TypedArray<uint32_t> _header_stampnsec_arr = arr[0]["nsec"];
        val.nsec = _header_stampnsec_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'nsec' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'nsec' is wrong type; expected a uint32.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T get_arr_ros_Time(MDFactory_T& factory, const std_msgs::Header::_stamp_type& val) {
    auto _header_stampoutArray = factory.createStructArray({1,1},{"sec","nsec"});
    // _ros_Time.sec
    _header_stampoutArray[0]["sec"] = factory.createScalar(val.sec);
    // _ros_Time.nsec
    _header_stampoutArray[0]["nsec"] = factory.createScalar(val.nsec);
    return std::move(_header_stampoutArray);
  }
  //----------------------------------------------------------------------------
  void copy_from_arr_sensor_msgs_JointState(sensor_msgs::JointState& val, const matlab::data::StructArray& arr) {
    // _sensor_msgs_JointState.header
    try {
        const matlab::data::StructArray _jointstateheader_arr = arr[0]["header"];
        copy_from_arr_std_msgs_Header(val.header,_jointstateheader_arr);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'header' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'header' is wrong type; expected a struct.");
    }
    // _sensor_msgs_JointState.name
    try {
        const matlab::data::CellArray _jointstatename_cellarr = arr[0]["name"];
        size_t nelem = _jointstatename_cellarr.getNumberOfElements();
        for (size_t idx=0; idx < nelem; ++idx){
        	const matlab::data::CharArray _jointstatename_arr = _jointstatename_cellarr[idx];
        	val.name.push_back(_jointstatename_arr.toAscii());
        }
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'name' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'name' is wrong type; expected a string.");
    }
    // _sensor_msgs_JointState.position
    try {
        const matlab::data::TypedArray<double> _jointstateposition_arr = arr[0]["position"];
        size_t nelem = _jointstateposition_arr.getNumberOfElements();
        	val.position.resize(nelem);
        	std::copy(_jointstateposition_arr.begin(), _jointstateposition_arr.begin()+nelem, val.position.begin());
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'position' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'position' is wrong type; expected a double.");
    }
    // _sensor_msgs_JointState.velocity
    try {
        const matlab::data::TypedArray<double> _jointstatevelocity_arr = arr[0]["velocity"];
        size_t nelem = _jointstatevelocity_arr.getNumberOfElements();
        	val.velocity.resize(nelem);
        	std::copy(_jointstatevelocity_arr.begin(), _jointstatevelocity_arr.begin()+nelem, val.velocity.begin());
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'velocity' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'velocity' is wrong type; expected a double.");
    }
    // _sensor_msgs_JointState.effort
    try {
        const matlab::data::TypedArray<double> _jointstateeffort_arr = arr[0]["effort"];
        size_t nelem = _jointstateeffort_arr.getNumberOfElements();
        	val.effort.resize(nelem);
        	std::copy(_jointstateeffort_arr.begin(), _jointstateeffort_arr.begin()+nelem, val.effort.begin());
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'effort' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'effort' is wrong type; expected a double.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T get_arr_sensor_msgs_JointState(MDFactory_T& factory, const sam_custom_messages::robot_state::_jointstate_type& val) {
    auto _jointstateoutArray = factory.createStructArray({1,1},{"header","name","position","velocity","effort"});
    // _sensor_msgs_JointState.header
    _jointstateoutArray[0]["header"] = get_arr_std_msgs_Header(factory, val.header);
    // _sensor_msgs_JointState.name
    auto _jointstatenameoutCell = factory.createCellArray({1,val.name.size()});
    for(size_t idxin = 0; idxin < val.name.size(); ++ idxin){
    	_jointstatenameoutCell[idxin] = factory.createCharArray(val.name[idxin]);
    }
    _jointstateoutArray[0]["name"] = _jointstatenameoutCell;
    // _sensor_msgs_JointState.position
    _jointstateoutArray[0]["position"] = factory.createArray<sensor_msgs::JointState::_position_type::const_iterator, double>({1, val.position.size()}, val.position.begin(), val.position.end());
    // _sensor_msgs_JointState.velocity
    _jointstateoutArray[0]["velocity"] = factory.createArray<sensor_msgs::JointState::_velocity_type::const_iterator, double>({1, val.velocity.size()}, val.velocity.begin(), val.velocity.end());
    // _sensor_msgs_JointState.effort
    _jointstateoutArray[0]["effort"] = factory.createArray<sensor_msgs::JointState::_effort_type::const_iterator, double>({1, val.effort.size()}, val.effort.begin(), val.effort.end());
    return std::move(_jointstateoutArray);
  }
  //----------------------------------------------------------------------------
  void copy_from_arr_geometry_msgs_Pose(geometry_msgs::Pose& val, const matlab::data::StructArray& arr) {
    // _geometry_msgs_Pose.position
    try {
        const matlab::data::StructArray _poseposition_arr = arr[0]["position"];
        copy_from_arr_geometry_msgs_Point(val.position,_poseposition_arr);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'position' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'position' is wrong type; expected a struct.");
    }
    // _geometry_msgs_Pose.orientation
    try {
        const matlab::data::StructArray _poseorientation_arr = arr[0]["orientation"];
        copy_from_arr_geometry_msgs_Quaternion(val.orientation,_poseorientation_arr);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'orientation' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'orientation' is wrong type; expected a struct.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T get_arr_geometry_msgs_Pose(MDFactory_T& factory, const sam_custom_messages::robot_state::_pose_type& val) {
    auto _poseoutArray = factory.createStructArray({1,1},{"position","orientation"});
    // _geometry_msgs_Pose.position
    _poseoutArray[0]["position"] = get_arr_geometry_msgs_Point(factory, val.position);
    // _geometry_msgs_Pose.orientation
    _poseoutArray[0]["orientation"] = get_arr_geometry_msgs_Quaternion(factory, val.orientation);
    return std::move(_poseoutArray);
  }
  //----------------------------------------------------------------------------
  void copy_from_arr_geometry_msgs_Point(geometry_msgs::Point& val, const matlab::data::StructArray& arr) {
    // _geometry_msgs_Point.x
    try {
        const matlab::data::TypedArray<double> _pose_positionx_arr = arr[0]["x"];
        val.x = _pose_positionx_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'x' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'x' is wrong type; expected a double.");
    }
    // _geometry_msgs_Point.y
    try {
        const matlab::data::TypedArray<double> _pose_positiony_arr = arr[0]["y"];
        val.y = _pose_positiony_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'y' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'y' is wrong type; expected a double.");
    }
    // _geometry_msgs_Point.z
    try {
        const matlab::data::TypedArray<double> _pose_positionz_arr = arr[0]["z"];
        val.z = _pose_positionz_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'z' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'z' is wrong type; expected a double.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T get_arr_geometry_msgs_Point(MDFactory_T& factory, const geometry_msgs::Pose::_position_type& val) {
    auto _pose_positionoutArray = factory.createStructArray({1,1},{"x","y","z"});
    // _geometry_msgs_Point.x
    _pose_positionoutArray[0]["x"] = factory.createScalar(val.x);
    // _geometry_msgs_Point.y
    _pose_positionoutArray[0]["y"] = factory.createScalar(val.y);
    // _geometry_msgs_Point.z
    _pose_positionoutArray[0]["z"] = factory.createScalar(val.z);
    return std::move(_pose_positionoutArray);
  }
  //----------------------------------------------------------------------------
  void copy_from_arr_geometry_msgs_Quaternion(geometry_msgs::Quaternion& val, const matlab::data::StructArray& arr) {
    // _geometry_msgs_Quaternion.x
    try {
        const matlab::data::TypedArray<double> _pose_orientationx_arr = arr[0]["x"];
        val.x = _pose_orientationx_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'x' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'x' is wrong type; expected a double.");
    }
    // _geometry_msgs_Quaternion.y
    try {
        const matlab::data::TypedArray<double> _pose_orientationy_arr = arr[0]["y"];
        val.y = _pose_orientationy_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'y' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'y' is wrong type; expected a double.");
    }
    // _geometry_msgs_Quaternion.z
    try {
        const matlab::data::TypedArray<double> _pose_orientationz_arr = arr[0]["z"];
        val.z = _pose_orientationz_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'z' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'z' is wrong type; expected a double.");
    }
    // _geometry_msgs_Quaternion.w
    try {
        const matlab::data::TypedArray<double> _pose_orientationw_arr = arr[0]["w"];
        val.w = _pose_orientationw_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'w' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'w' is wrong type; expected a double.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T get_arr_geometry_msgs_Quaternion(MDFactory_T& factory, const geometry_msgs::Pose::_orientation_type& val) {
    auto _pose_orientationoutArray = factory.createStructArray({1,1},{"x","y","z","w"});
    // _geometry_msgs_Quaternion.x
    _pose_orientationoutArray[0]["x"] = factory.createScalar(val.x);
    // _geometry_msgs_Quaternion.y
    _pose_orientationoutArray[0]["y"] = factory.createScalar(val.y);
    // _geometry_msgs_Quaternion.z
    _pose_orientationoutArray[0]["z"] = factory.createScalar(val.z);
    // _geometry_msgs_Quaternion.w
    _pose_orientationoutArray[0]["w"] = factory.createScalar(val.w);
    return std::move(_pose_orientationoutArray);
  }
  //----------------------------------------------------------------------------
  SAM_CUSTOM_MESSAGES_EXPORT void copy_from_arr(boost::shared_ptr<sam_custom_messages::robot_state>& msg, const matlab::data::StructArray arr) {
    try {
        //header
        const matlab::data::StructArray header_arr = arr[0]["header"];
        copy_from_arr_std_msgs_Header(msg->header,header_arr);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'header' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'header' is wrong type; expected a struct.");
    }
    try {
        //user_id
        const matlab::data::TypedArray<int8_t> user_id_arr = arr[0]["user_id"];
        msg->user_id = user_id_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'user_id' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'user_id' is wrong type; expected a int8.");
    }
    try {
        //jointstate
        const matlab::data::StructArray jointstate_arr = arr[0]["jointstate"];
        copy_from_arr_sensor_msgs_JointState(msg->jointstate,jointstate_arr);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'jointstate' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'jointstate' is wrong type; expected a struct.");
    }
    try {
        //pose
        const matlab::data::StructArray pose_arr = arr[0]["pose"];
        copy_from_arr_geometry_msgs_Pose(msg->pose,pose_arr);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'pose' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'pose' is wrong type; expected a struct.");
    }
  }
  //----------------------------------------------------------------------------
  SAM_CUSTOM_MESSAGES_EXPORT MDArray_T get_arr(MDFactory_T& factory, const boost::shared_ptr<const sam_custom_messages::robot_state>& msg) {
    auto outArray = factory.createStructArray({1,1},{"header","user_id","jointstate","pose"});
    // header
    outArray[0]["header"] = get_arr_std_msgs_Header(factory, msg->header);
    // user_id
    outArray[0]["user_id"] = factory.createScalar(msg->user_id);
    // jointstate
    outArray[0]["jointstate"] = get_arr_sensor_msgs_JointState(factory, msg->jointstate);
    // pose
    outArray[0]["pose"] = get_arr_geometry_msgs_Pose(factory, msg->pose);
    return std::move(outArray);
  }
} //namespace robot_state
} //namespace matlabhelper
} //namespace sam_custom_messages
#ifdef _MSC_VER
#pragma warning(pop)
#else
#pragma GCC diagnostic pop
#endif //_MSC_VER
//gen-1