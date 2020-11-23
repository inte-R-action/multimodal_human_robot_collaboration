// Generated by gencpp from file sam_custom_messages/user_prediction.msg
// DO NOT EDIT!


#ifndef SAM_CUSTOM_MESSAGES_MESSAGE_USER_PREDICTION_H
#define SAM_CUSTOM_MESSAGES_MESSAGE_USER_PREDICTION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace sam_custom_messages
{
template <class ContainerAllocator>
struct user_prediction_
{
  typedef user_prediction_<ContainerAllocator> Type;

  user_prediction_()
    : header()
    , user_id(0)
    , predictions()  {
    }
  user_prediction_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , user_id(0)
    , predictions(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int8_t _user_id_type;
  _user_id_type user_id;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _predictions_type;
  _predictions_type predictions;





  typedef boost::shared_ptr< ::sam_custom_messages::user_prediction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sam_custom_messages::user_prediction_<ContainerAllocator> const> ConstPtr;

}; // struct user_prediction_

typedef ::sam_custom_messages::user_prediction_<std::allocator<void> > user_prediction;

typedef boost::shared_ptr< ::sam_custom_messages::user_prediction > user_predictionPtr;
typedef boost::shared_ptr< ::sam_custom_messages::user_prediction const> user_predictionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sam_custom_messages::user_prediction_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sam_custom_messages::user_prediction_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sam_custom_messages::user_prediction_<ContainerAllocator1> & lhs, const ::sam_custom_messages::user_prediction_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.user_id == rhs.user_id &&
    lhs.predictions == rhs.predictions;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sam_custom_messages::user_prediction_<ContainerAllocator1> & lhs, const ::sam_custom_messages::user_prediction_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sam_custom_messages

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sam_custom_messages::user_prediction_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sam_custom_messages::user_prediction_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sam_custom_messages::user_prediction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sam_custom_messages::user_prediction_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sam_custom_messages::user_prediction_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sam_custom_messages::user_prediction_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sam_custom_messages::user_prediction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "546e38fb2a5d19f634c167b97894dce3";
  }

  static const char* value(const ::sam_custom_messages::user_prediction_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x546e38fb2a5d19f6ULL;
  static const uint64_t static_value2 = 0x34c167b97894dce3ULL;
};

template<class ContainerAllocator>
struct DataType< ::sam_custom_messages::user_prediction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sam_custom_messages/user_prediction";
  }

  static const char* value(const ::sam_custom_messages::user_prediction_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sam_custom_messages::user_prediction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "## Message containing predictions of what user capability will be performed next\n"
"#\n"
"## std_msgs/Header.msg\n"
"# sequence ID: consecutively increasing ID \n"
"# uint32 seq\n"
"# Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"# time stamp\n"
"# Frame this data is associated with\n"
"# string frame_id\n"
"Header header\n"
"#\n"
"## ID of user (robot or human)\n"
"int8 user_id\n"
"#\n"
"## Probabilities of future capabilities being next\n"
"float64[] predictions\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::sam_custom_messages::user_prediction_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sam_custom_messages::user_prediction_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.user_id);
      stream.next(m.predictions);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct user_prediction_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sam_custom_messages::user_prediction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sam_custom_messages::user_prediction_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "user_id: ";
    Printer<int8_t>::stream(s, indent + "  ", v.user_id);
    s << indent << "predictions[]" << std::endl;
    for (size_t i = 0; i < v.predictions.size(); ++i)
    {
      s << indent << "  predictions[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.predictions[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SAM_CUSTOM_MESSAGES_MESSAGE_USER_PREDICTION_H
