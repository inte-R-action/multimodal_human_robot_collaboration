// Copyright 2019-2020 The MathWorks, Inc.
// Common copy functions for sam_custom_messages/diagnostics
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
#include "sam_custom_messages/diagnostics.h"
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
namespace diagnostics {
  void copy_from_arr_std_msgs_Header(std_msgs::Header& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_std_msgs_Header(MDFactory_T& factory, const sam_custom_messages::diagnostics::_header_type& val);
  void copy_from_arr_ros_Time(ros::Time& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_ros_Time(MDFactory_T& factory, const std_msgs::Header::_stamp_type& val);
  void copy_from_arr_diagnostic_msgs_DiagnosticStatus(diagnostic_msgs::DiagnosticStatus& val, const matlab::data::StructArray& arr);
  MDArray_T get_arr_diagnostic_msgs_DiagnosticStatus(MDFactory_T& factory, const sam_custom_messages::diagnostics::_diagnosticstatus_type& val);
  void copy_from_arr_diagnostic_msgs_KeyValue_var_arr(diagnostic_msgs::KeyValue& val, const matlab::data::Struct& arr);
  MDArray_T get_arr_diagnostic_msgs_KeyValue_var_arr(MDFactory_T& factory, const diagnostic_msgs::DiagnosticStatus::_values_type& val);
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
  MDArray_T get_arr_std_msgs_Header(MDFactory_T& factory, const sam_custom_messages::diagnostics::_header_type& val) {
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
  void copy_from_arr_diagnostic_msgs_DiagnosticStatus(diagnostic_msgs::DiagnosticStatus& val, const matlab::data::StructArray& arr) {
    // _diagnostic_msgs_DiagnosticStatus.OK
    // _diagnostic_msgs_DiagnosticStatus.WARN
    // _diagnostic_msgs_DiagnosticStatus.ERROR
    // _diagnostic_msgs_DiagnosticStatus.STALE
    // _diagnostic_msgs_DiagnosticStatus.level
    try {
        const matlab::data::TypedArray<int8_t> _diagnosticstatuslevel_arr = arr[0]["level"];
        val.level = _diagnosticstatuslevel_arr[0];
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'level' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'level' is wrong type; expected a int8.");
    }
    // _diagnostic_msgs_DiagnosticStatus.name
    try {
        const matlab::data::CharArray _diagnosticstatusname_arr = arr[0]["name"];
        val.name = _diagnosticstatusname_arr.toAscii();
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'name' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'name' is wrong type; expected a string.");
    }
    // _diagnostic_msgs_DiagnosticStatus.message
    try {
        const matlab::data::CharArray _diagnosticstatusmessage_arr = arr[0]["message"];
        val.message = _diagnosticstatusmessage_arr.toAscii();
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'message' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'message' is wrong type; expected a string.");
    }
    // _diagnostic_msgs_DiagnosticStatus.hardware_id
    try {
        const matlab::data::CharArray _diagnosticstatushardware_id_arr = arr[0]["hardware_id"];
        val.hardware_id = _diagnosticstatushardware_id_arr.toAscii();
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'hardware_id' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'hardware_id' is wrong type; expected a string.");
    }
    // _diagnostic_msgs_DiagnosticStatus.values
    try {
        const matlab::data::StructArray _diagnosticstatusvalues_arr = arr[0]["values"];
        for (auto _valuesarr : _diagnosticstatusvalues_arr) {
        	diagnostic_msgs::KeyValue _val;
        	copy_from_arr_diagnostic_msgs_KeyValue_var_arr(_val,_valuesarr);
        	val.values.push_back(_val);
        }
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'values' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'values' is wrong type; expected a struct.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T get_arr_diagnostic_msgs_DiagnosticStatus(MDFactory_T& factory, const sam_custom_messages::diagnostics::_diagnosticstatus_type& val) {
    auto _diagnosticstatusoutArray = factory.createStructArray({1,1},{"OK","WARN","ERROR","STALE","level","name","message","hardware_id","values"});
    // _diagnostic_msgs_DiagnosticStatus.OK
    _diagnosticstatusoutArray[0]["OK"] = factory.createScalar(static_cast<int8_t>(val.OK));
    // _diagnostic_msgs_DiagnosticStatus.WARN
    _diagnosticstatusoutArray[0]["WARN"] = factory.createScalar(static_cast<int8_t>(val.WARN));
    // _diagnostic_msgs_DiagnosticStatus.ERROR
    _diagnosticstatusoutArray[0]["ERROR"] = factory.createScalar(static_cast<int8_t>(val.ERROR));
    // _diagnostic_msgs_DiagnosticStatus.STALE
    _diagnosticstatusoutArray[0]["STALE"] = factory.createScalar(static_cast<int8_t>(val.STALE));
    // _diagnostic_msgs_DiagnosticStatus.level
    _diagnosticstatusoutArray[0]["level"] = factory.createScalar(val.level);
    // _diagnostic_msgs_DiagnosticStatus.name
    _diagnosticstatusoutArray[0]["name"] = factory.createCharArray(val.name);
    // _diagnostic_msgs_DiagnosticStatus.message
    _diagnosticstatusoutArray[0]["message"] = factory.createCharArray(val.message);
    // _diagnostic_msgs_DiagnosticStatus.hardware_id
    _diagnosticstatusoutArray[0]["hardware_id"] = factory.createCharArray(val.hardware_id);
    // _diagnostic_msgs_DiagnosticStatus.values
    _diagnosticstatusoutArray[0]["values"] = get_arr_diagnostic_msgs_KeyValue_var_arr(factory, val.values);
    return std::move(_diagnosticstatusoutArray);
  }
  //----------------------------------------------------------------------------
  void copy_from_arr_diagnostic_msgs_KeyValue_var_arr(diagnostic_msgs::KeyValue& val, const matlab::data::Struct& arr) {
    // _diagnostic_msgs_KeyValue_var_arr.key
    try {
        const matlab::data::CharArray _diagnosticstatus_valueskey_arr = arr["key"];
        val.key = _diagnosticstatus_valueskey_arr.toAscii();
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'key' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'key' is wrong type; expected a string.");
    }
    // _diagnostic_msgs_KeyValue_var_arr.value
    try {
        const matlab::data::CharArray _diagnosticstatus_valuesvalue_arr = arr["value"];
        val.value = _diagnosticstatus_valuesvalue_arr.toAscii();
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'value' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'value' is wrong type; expected a string.");
    }
  }
  //----------------------------------------------------------------------------
  MDArray_T get_arr_diagnostic_msgs_KeyValue_var_arr(MDFactory_T& factory, const diagnostic_msgs::DiagnosticStatus::_values_type& val) {
    auto _diagnosticstatus_valuesoutArray = factory.createStructArray({1,val.size()},{"key","value"});
    for (size_t idx = 0; idx < val.size(); ++idx){
    // _diagnostic_msgs_KeyValue_var_arr.key
    	_diagnosticstatus_valuesoutArray[idx]["key"] = factory.createCharArray(val[idx].key);
    // _diagnostic_msgs_KeyValue_var_arr.value
    	_diagnosticstatus_valuesoutArray[idx]["value"] = factory.createCharArray(val[idx].value);
    }
    return std::move(_diagnosticstatus_valuesoutArray);
  }
  //----------------------------------------------------------------------------
  SAM_CUSTOM_MESSAGES_EXPORT void copy_from_arr(boost::shared_ptr<sam_custom_messages::diagnostics>& msg, const matlab::data::StructArray arr) {
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
        //diagnosticstatus
        const matlab::data::StructArray diagnosticstatus_arr = arr[0]["diagnosticstatus"];
        copy_from_arr_diagnostic_msgs_DiagnosticStatus(msg->diagnosticstatus,diagnosticstatus_arr);
    } catch (matlab::data::InvalidFieldNameException&) {
        throw std::invalid_argument("Field 'diagnosticstatus' is missing.");
    } catch (matlab::data::TypeMismatchException&) {
        throw std::invalid_argument("Field 'diagnosticstatus' is wrong type; expected a struct.");
    }
  }
  //----------------------------------------------------------------------------
  SAM_CUSTOM_MESSAGES_EXPORT MDArray_T get_arr(MDFactory_T& factory, const boost::shared_ptr<const sam_custom_messages::diagnostics>& msg) {
    auto outArray = factory.createStructArray({1,1},{"header","user_id","diagnosticstatus"});
    // header
    outArray[0]["header"] = get_arr_std_msgs_Header(factory, msg->header);
    // user_id
    outArray[0]["user_id"] = factory.createScalar(msg->user_id);
    // diagnosticstatus
    outArray[0]["diagnosticstatus"] = get_arr_diagnostic_msgs_DiagnosticStatus(factory, msg->diagnosticstatus);
    return std::move(outArray);
  }
} //namespace diagnostics
} //namespace matlabhelper
} //namespace sam_custom_messages
#ifdef _MSC_VER
#pragma warning(pop)
#else
#pragma GCC diagnostic pop
#endif //_MSC_VER
//gen-1