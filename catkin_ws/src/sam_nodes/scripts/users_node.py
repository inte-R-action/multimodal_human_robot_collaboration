import rospy
import numpy as np
from std_msgs.msg import String
from user import User
from sam_custom_messages import hand_pos, capability, current_action, diagnostics, user_prediction

diag_msg = diagnostics
diag_msg.Header.Stamp = rospy.get_rostime()
diag_msg.Header.Seq = 0
diag_msg.Header.FrameId = 
diag_msg.UserId
diag_msg.UserName
diag_msg.Diagnosticstatus.Level
diag_msg.Diagnosticstatus.Name
diag_msg.Diagnosticstatus.Message
diag_msg.Diagnosticstatus.HardwareId
diag_msg.Diagnosticstatus.values.key
diag_msg.Diagnosticstatus.values.value

def setup_user(name=None):

    id = len(users)
    if name is None:
        name = f"unknown_user_{id}"
    
    users.append[User(name, id)]

def hand_pos_callback(data):
    if users[data.UserId].name != data.UserName:
        print(f"ERROR: users list name {users[data.UserId].name} does not match hand_pos msg name {data.UserName}")
    else:
        if data.Hand == 0:
            self.left_h_pos = [Pose.Position.X, Pose.Position.Y, Pose.Position.Z]
            self.left_h_rot = [Pose.Orientation.X, Pose.Orientation.Y, Pose.Orientation.Z, Pose.Orientation.W]      
        elif data.Hand == 1:
            self.right_h_pos = [Pose.Position.X, Pose.Position.Y, Pose.Position.Z]
            self.right_h_rot = [Pose.Orientation.X, Pose.Orientation.Y, Pose.Orientation.Z, Pose.Orientation.W]
        else:
            print(f"ERROR: hand_pos.hand msg is {data.Hand} but should be 0 (left) or 1 (right)")

    return
    

def current_action_callback(data):
    if users[data.UserId].name != data.UserName:
        print(f"ERROR: users list name {users[data.UserId].name} does not match current_action msg name {data.UserName}")
    else:
        users[data.UserId].current_action = data.action_probs

    return

def users_node():

    rospy.init_node('users_node', anonymous=True)

    status_pub = rospy.Publisher('SystemStatus', diagnostics, queue_size=10)
    future_pub = rospy.Publisher('FutureState', user_prediction, queue_size=10)
    
    rospy.Subscriber("HandStates", hand_pos, hand_pos_callback)
    rospy.Subscriber("CurrentAction", current_action, current_action_callback)

    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)

        status_pub.publish(
                            )
        
        rate.sleep()

if __name__ == '__main__':
    try:
        users_node()
    except rospy.ROSInterruptException:
        pass