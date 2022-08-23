## Message containing current and last fastener counts
#
## std_msgs/Header.msg
# sequence ID: consecutively increasing ID 
# uint32 seq
# Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
# time stamp
# Frame this data is associated with
# string frame_id
Header Header
#
## ID of user (robot or human)
int8 UserId
#
## Name of user (robot or human)
string UserName
#
## Current number of fasteners
int8 FastenerCount
#
## Last number of fasteners
int8 LastFastenerCount