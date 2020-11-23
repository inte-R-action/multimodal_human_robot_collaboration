%setenv('ROS_HOSTNAME', '169.254.241.77')
%setenv('ROS_IP', '169.254.241.83')
%setenv('ROS_MASTER_URI', 'http://169.254.241.83:11311')
%rosinit
rosinit('169.254.241.83')

chatterpub = rospublisher('/chatter', 'std_msgs/String');
pause(2) % Wait to ensure publisher is registered
chattermsg = rosmessage(chatterpub);
chattermsg.Data = 'hello world';

getenv('ROS_MASTER_URI')
getenv('ROS_HOSTNAME')
getenv('ROS_IP')

x = 0;
while x < 50
    send(chatterpub,chattermsg)
    pause(2)
    x = x + 1;
end

rosshutdown
