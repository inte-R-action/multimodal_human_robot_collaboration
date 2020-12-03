function recv_hand(name, data, frame, time)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
global hand_pub_msg

hand_pub_msg.Header.Stamp = rostime('now');
hand_pub_msg.Header.Seq = 0;
hand_pub_msg.Header.FrameId = sprintf('mocap %i', frame);

hand_pub_msg.UserId = 0;
hand_pub_msg.UserName = strtok(name,'_');
if name(end) == 'R'
    hand_pub_msg.Hand = 1;
elseif name(end) == 'L'
    hand_pub_msg.Hand = 0;
end

hand_pub_msg.Pose.Orientation.X = data.qx;
hand_pub_msg.Pose.Orientation.Y = data.qy;
hand_pub_msg.Pose.Orientation.Z = data.qz;
hand_pub_msg.Pose.Orientation.W = data.qw;

hand_pub_msg.Pose.Position.X = data.x * 1000;
hand_pub_msg.Pose.Position.Y = data.y * 1000;
hand_pub_msg.Pose.Position.Z = data.z * 1000;
end

