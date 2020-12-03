function recv_rigidbody(name, data, frame, time)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
global object_pub_msg

object_pub_msg.Header.Stamp = rostime('now');
object_pub_msg.Header.Seq = 0;
object_pub_msg.Header.FrameId = sprintf('mocap %i', frame);

object_pub_msg.Object.Id = 0;
object_pub_msg.Object.Type = 0;
obj_info = cellstr(name);
object_pub_msg.Object.Info = obj_info;

object_pub_msg.Pose.Orientation.X = data.qx;
object_pub_msg.Pose.Orientation.Y = data.qy;
object_pub_msg.Pose.Orientation.Z = data.qz;
object_pub_msg.Pose.Orientation.W = data.qw;

object_pub_msg.Pose.Position.X = data.x * 1000;
object_pub_msg.Pose.Position.Y = data.y * 1000;
object_pub_msg.Pose.Position.Z = data.z * 1000;
end

