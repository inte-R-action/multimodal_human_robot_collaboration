global object_state_pub object_pub_msg model hand_state_pub hand_pub_msg mocap_state_pub diagnostics_pub_msg%robotpose


% Setup ROS Node
% --- Start Matlab Global Node  
try
    rosnode list
catch exp   % Error from rosnode list
    rosinit('169.254.241.83');  % only if error: rosinit
end
object_state_pub = rospublisher('/ObjectStates', 'sam_custom_messages/object_state');
hand_state_pub = rospublisher('/HandStates', 'sam_custom_messages/hand_pos');
mocap_state_pub = rospublisher('/SystemStatus', 'sam_custom_messages/diagnostics');
%robotpose = rossubscriber('/SensorStates', @natnet_sub_callback);
pause(2) % Wait to ensure publisher is registered

object_pub_msg = rosmessage(object_state_pub);
hand_pub_msg = rosmessage(hand_state_pub);
diagnostics_pub_msg = rosmessage(mocap_state_pub);
%chattermsg.Data = 'hello world'; 
send(object_state_pub, object_pub_msg)
send(hand_state_pub, hand_pub_msg)
send(mocap_state_pub, diagnostics_pub_msg)
pause(2)


% Create NatNet Client
natnetclient = natnet;
% connect the client to the server (multicast over local loopback) -
% modify for your network
fprintf( 'Connecting to the server\n' )
natnetclient.HostIP = '127.0.0.1';
natnetclient.ClientIP = '127.0.0.1';
natnetclient.ConnectionType = 'Multicast';
natnetclient.connect;
if ( natnetclient.IsConnected == 0 )
    fprintf( 'Client failed to connect\n' )
    fprintf( '\tMake sure the host is connected to the network\n' )
    fprintf( '\tand that the host and client IP addresses are correct\n\n' )
    return
end
model = natnetclient.getModelDescription;

% add some callback functions that execute autmatically in an
% asynchronous manner to the event of a new frame of mocap data,
% similar to how software interrupts operate.
% callback functions block further execution of running code and a event handler buffer is created
% with pending function callbacks to execute. Matlab by default is single threaded.
% callbacks are added to the event handler buffer in no particular order.
fprintf( 'Adding callback functions to execute with each frame of mocap\n' )
addpath( 'event_handlers')
% first input is the listener slot and the second is the function
% name, which must be an m file on the Matlab Path or current folder.
natnetclient.addlistener( 1 , 'natnet_event_callback');

% by default listeners/interrupts are disabled in the natnet class.
% enable all listeners, 0, or individual listeners, 1, 2, etc.
% Similiar for disabling
fprintf( 'Enabling the listeners for asynchronous callback execution\n' )

natnetclient.enable(0)
r = rosrate(1);
reset(r)

f = figure('Position',[500 500 400 300]);
c = uicontrol('String','Exit','Callback','closereq');

 while size(findobj(f)) > 0
	time = r.TotalElapsedTime;
    
	fprintf('Time Elapsed: %f \n',time)
    diagnostic_send()
    send(mocap_state_pub, diagnostics_pub_msg)
	waitfor(r);
    
end

disp('Closing down');

fprintf( 'Disabling the listeners\n')
natnetclient.disable(0)
disp('NatNet Event Handler Sample End' )
pause(3)
clear global pos orient
rosshutdown




