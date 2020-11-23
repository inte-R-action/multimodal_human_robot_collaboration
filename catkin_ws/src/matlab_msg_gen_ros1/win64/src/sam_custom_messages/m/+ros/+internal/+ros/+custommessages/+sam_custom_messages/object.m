function [data, info] = object
%Object gives an empty data for sam_custom_messages/Object
% Copyright 2019-2020 The MathWorks, Inc.
data = struct();
[data.id, info.id] = ros.internal.ros.messages.ros.default_type('int8',1);
[data.type, info.type] = ros.internal.ros.messages.ros.default_type('int8',1);
[data.info, info.info] = ros.internal.ros.messages.ros.char('string',NaN);
info.MessageType = 'sam_custom_messages/Object';
info.constant = 0;
info.default = 0;
info.maxstrlen = NaN;
info.MaxLen = 1;
info.MinLen = 1;
info.MatPath = cell(1,3);
info.MatPath{1} = 'id';
info.MatPath{2} = 'type';
info.MatPath{3} = 'info';
