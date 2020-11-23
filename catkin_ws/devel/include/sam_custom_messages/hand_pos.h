// Generated by gencpp from file sam_custom_messages/hand_pos.msg
// DO NOT EDIT!


#ifndef SAM_CUSTOM_MESSAGES_MESSAGE_HAND_POS_H
#define SAM_CUSTOM_MESSAGES_MESSAGE_HAND_POS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Pose.h>

namespace sam_custom_messages
{
template <class ContainerAllocator>
struct hand_pos_
{
  typedef hand_pos_<ContainerAllocator> Type;

  hand_pos_()
    : header()
    , user_id(0)
    , user_name()
    , hand(0)
    , pose()  {
    }
  hand_pos_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , user_id(0)
    , user_name(_alloc)
    , hand(0)
    , pose(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int8_t _user_id_type;
  _user_id_type user_id;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _user_name_type;
  _user_name_type user_name;

   typedef int8_t _hand_type;
  _hand_type hand;

   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _pose_type;
  _pose_type pose;





  typedef boost::shared_ptr< ::sam_custom_messages::hand_pos_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sam_custom_messages::hand_pos_<ContainerAllocator> const> ConstPtr;

}; // struct hand_pos_

typedef ::sam_custom_messages::hand_pos_<std::allocator<void> > hand_pos;

typedef boost::shared_ptr< ::sam_custom_messages::hand_pos > hand_posPtr;
typedef boost::shared_ptr< ::sam_custom_messages::hand_pos const> hand_posConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sam_custom_messages::hand_pos_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sam_custom_messages::hand_pos_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sam_custom_messages::hand_pos_<ContainerAllocator1> & lhs, const ::sam_custom_messages::hand_pos_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.user_id == rhs.user_id &&
    lhs.user_name == rhs.user_name &&
    lhs.hand == rhs.hand &&
    lhs.pose == rhs.pose;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sam_custom_messages::hand_pos_<ContainerAllocator1> & lhs, const ::sam_custom_messages::hand_pos_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sam_custom_messages

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sam_custom_messages::hand_pos_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sam_custom_messages::hand_pos_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sam_custom_messages::hand_pos_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sam_custom_messages::hand_pos_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sam_custom_messages::hand_pos_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sam_custom_messages::hand_pos_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sam_custom_messages::hand_pos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1c6006785295f1dfe86ef734b697fe78";
  }

  static const char* value(const ::sam_custom_messages::hand_pos_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1c6006785295f1dfULL;
  static const uint64_t static_value2 = 0xe86ef734b697fe78ULL;
};

template<class ContainerAllocator>
struct DataType< ::sam_custom_messages::hand_pos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sam_custom_messages/hand_pos";
  }

  static const char* value(const ::sam_custom_messages::hand_pos_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sam_custom_messages::hand_pos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "## Message containing location of a users hand\n"
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
"## Name of user (robot or human)\n"
"string user_name\n"
"#\n"
"## Which hand location is for, 0:left, 1:right\n"
"int8 hand\n"
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

  static const char* value(const ::sam_custom_messages::hand_pos_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sam_custom_messages::hand_pos_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.user_id);
      stream.next(m.user_name);
      stream.next(m.hand);
      stream.next(m.pose);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct hand_pos_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sam_custom_messages::hand_pos_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sam_custom_messages::hand_pos_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "user_id: ";
    Printer<int8_t>::stream(s, indent + "  ", v.user_id);
    s << indent << "user_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.user_name);
    s << indent << "hand: ";
    Printer<int8_t>::stream(s, indent + "  ", v.hand);
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SAM_CUSTOM_MESSAGES_MESSAGE_HAND_POS_H
