// Generated by gencpp from file sam_custom_messages/object_state.msg
// DO NOT EDIT!


#ifndef SAM_CUSTOM_MESSAGES_MESSAGE_OBJECT_STATE_H
#define SAM_CUSTOM_MESSAGES_MESSAGE_OBJECT_STATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <sam_custom_messages/Object.h>
#include <geometry_msgs/Pose.h>

namespace sam_custom_messages
{
template <class ContainerAllocator>
struct object_state_
{
  typedef object_state_<ContainerAllocator> Type;

  object_state_()
    : header()
    , object()
    , pose()  {
    }
  object_state_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , object(_alloc)
    , pose(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::sam_custom_messages::Object_<ContainerAllocator>  _object_type;
  _object_type object;

   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _pose_type;
  _pose_type pose;





  typedef boost::shared_ptr< ::sam_custom_messages::object_state_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sam_custom_messages::object_state_<ContainerAllocator> const> ConstPtr;

}; // struct object_state_

typedef ::sam_custom_messages::object_state_<std::allocator<void> > object_state;

typedef boost::shared_ptr< ::sam_custom_messages::object_state > object_statePtr;
typedef boost::shared_ptr< ::sam_custom_messages::object_state const> object_stateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sam_custom_messages::object_state_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sam_custom_messages::object_state_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sam_custom_messages::object_state_<ContainerAllocator1> & lhs, const ::sam_custom_messages::object_state_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.object == rhs.object &&
    lhs.pose == rhs.pose;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sam_custom_messages::object_state_<ContainerAllocator1> & lhs, const ::sam_custom_messages::object_state_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sam_custom_messages

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sam_custom_messages::object_state_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sam_custom_messages::object_state_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sam_custom_messages::object_state_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sam_custom_messages::object_state_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sam_custom_messages::object_state_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sam_custom_messages::object_state_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sam_custom_messages::object_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2219f508c564a641c1ef4997ea740e7e";
  }

  static const char* value(const ::sam_custom_messages::object_state_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2219f508c564a641ULL;
  static const uint64_t static_value2 = 0xc1ef4997ea740e7eULL;
};

template<class ContainerAllocator>
struct DataType< ::sam_custom_messages::object_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sam_custom_messages/object_state";
  }

  static const char* value(const ::sam_custom_messages::object_state_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sam_custom_messages::object_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "## Message containing information on location, type and details about an object in the environment\n"
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
"## object.msg\n"
"# Information on object type and further details\n"
"# int8 id\n"
"# int8 type \n"
"# string[] info\n"
"Object object\n"
"#\n"
"# geometry_msgs/Pose.msg\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"# Point position\n"
"# Quaternion orientation\n"
"geometry_msgs/Pose pose\n"
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
"\n"
"================================================================================\n"
"MSG: sam_custom_messages/Object\n"
"# Message containg information on objects within environment\n"
"#\n"
"# Unique ID of object\n"
"int8 id\n"
"#\n"
"# Type of object ID\n"
"int8 type\n"
"#\n"
"# Additional information on object\n"
"string[] info\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::sam_custom_messages::object_state_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sam_custom_messages::object_state_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.object);
      stream.next(m.pose);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct object_state_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sam_custom_messages::object_state_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sam_custom_messages::object_state_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "object: ";
    s << std::endl;
    Printer< ::sam_custom_messages::Object_<ContainerAllocator> >::stream(s, indent + "  ", v.object);
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SAM_CUSTOM_MESSAGES_MESSAGE_OBJECT_STATE_H
