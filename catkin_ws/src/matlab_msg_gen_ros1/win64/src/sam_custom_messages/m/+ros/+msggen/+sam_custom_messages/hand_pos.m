
classdef hand_pos < ros.Message
    %hand_pos MATLAB implementation of sam_custom_messages/hand_pos
    %   This class was automatically generated by
    %   ros.internal.pubsubEmitter.
    %   Copyright 2014-2020 The MathWorks, Inc.
    properties (Constant)
        MessageType = 'sam_custom_messages/hand_pos' % The ROS message type
    end
    properties (Constant, Hidden)
        MD5Checksum = '1c6006785295f1dfe86ef734b697fe78' % The MD5 Checksum of the message definition
        PropertyList = { 'Header' 'Pose' 'UserId' 'UserName' 'Hand' } % List of non-constant message properties
        ROSPropertyList = { 'header' 'pose' 'user_id' 'user_name' 'hand' } % List of non-constant ROS message properties
        PropertyMessageTypes = { 'ros.msggen.std_msgs.Header' ...
			 'ros.msggen.geometry_msgs.Pose' ...
			 '' ...
			 '' ...
			 '' ...
			 } % Types of contained nested messages
    end
    properties (Constant)
    end
    properties
        Header
        Pose
        UserId
        UserName
        Hand
    end
    methods
        function set.Header(obj, val)
            validAttributes = {'nonempty', 'scalar'};
            validClasses = {'ros.msggen.std_msgs.Header'};
            validateattributes(val, validClasses, validAttributes, 'hand_pos', 'Header')
            obj.Header = val;
        end
        function set.Pose(obj, val)
            validAttributes = {'nonempty', 'scalar'};
            validClasses = {'ros.msggen.geometry_msgs.Pose'};
            validateattributes(val, validClasses, validAttributes, 'hand_pos', 'Pose')
            obj.Pose = val;
        end
        function set.UserId(obj, val)
            validClasses = {'numeric'};
            validAttributes = {'nonempty', 'scalar'};
            validateattributes(val, validClasses, validAttributes, 'hand_pos', 'UserId');
            obj.UserId = int8(val);
        end
        function set.UserName(obj, val)
            val = convertStringsToChars(val);
            validClasses = {'char', 'string'};
            validAttributes = {};
            validateattributes(val, validClasses, validAttributes, 'hand_pos', 'UserName');
            obj.UserName = char(val);
        end
        function set.Hand(obj, val)
            validClasses = {'numeric'};
            validAttributes = {'nonempty', 'scalar'};
            validateattributes(val, validClasses, validAttributes, 'hand_pos', 'Hand');
            obj.Hand = int8(val);
        end
    end
    methods (Static, Access = {?matlab.unittest.TestCase, ?ros.Message})
        function obj = loadobj(strObj)
        %loadobj Implements loading of message from MAT file
        % Return an empty object array if the structure element is not defined
            if isempty(strObj)
                obj = ros.msggen.sam_custom_messages.hand_pos.empty(0,1);
                return
            end
            % Create an empty message object
            obj = ros.msggen.sam_custom_messages.hand_pos;
            obj.reload(strObj);
        end
    end
end
