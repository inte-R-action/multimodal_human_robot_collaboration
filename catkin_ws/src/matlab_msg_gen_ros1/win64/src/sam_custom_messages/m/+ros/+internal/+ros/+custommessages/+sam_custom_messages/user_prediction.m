function [data, info] = user_prediction
%user_prediction gives an empty data for sam_custom_messages/user_prediction
% Copyright 2019-2020 The MathWorks, Inc.
data = struct();
[data.header, info.header] = ros.internal.ros.messages.std_msgs.header;
info.header.MLdataType = 'struct';
[data.user_id, info.user_id] = ros.internal.ros.messages.ros.default_type('int8',1);
[data.predictions, info.predictions] = ros.internal.ros.messages.ros.default_type('double',NaN);
info.MessageType = 'sam_custom_messages/user_prediction';
info.constant = 0;
info.default = 0;
info.maxstrlen = NaN;
info.MaxLen = 1;
info.MinLen = 1;
info.MatPath = cell(1,8);
info.MatPath{1} = 'header';
info.MatPath{2} = 'header.seq';
info.MatPath{3} = 'header.stamp';
info.MatPath{4} = 'header.stamp.sec';
info.MatPath{5} = 'header.stamp.nsec';
info.MatPath{6} = 'header.frame_id';
info.MatPath{7} = 'user_id';
info.MatPath{8} = 'predictions';
