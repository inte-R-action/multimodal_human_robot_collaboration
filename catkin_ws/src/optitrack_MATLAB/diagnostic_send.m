function diagnostic_send()
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
global diagnostics_pub_msg latest_evnt

diagnostics_pub_msg.Header.Stamp = rostime('now');%latest_evnt.fTimestamp
diagnostics_pub_msg.Header.Seq = 0;
try
    diagnostics_pub_msg.Header.FrameId = sprintf('mocap %i', latest_evnt.iFrame);
catch exp
    diagnostics_pub_msg.Header.FrameId = sprintf('mocap frame unknown');
end

diagnostics_pub_msg.UserId = 0;
%diagnostics_pub_msg.UserName = "N/A";

diagnostics_pub_msg.Diagnosticstatus.Level = 0;
diagnostics_pub_msg.Diagnosticstatus.Name = "Motion Capture";
diagnostics_pub_msg.Diagnosticstatus.Message = "tbc";
diagnostics_pub_msg.Diagnosticstatus.HardwareId = "tbc";
%diagnostics_pub_msg.Diagnosticstatus.Values.Value = "tbc";
%diagnostics_pub_msg.Diagnosticstatus.Values.Key = "tbc";
%diagnostics_pub_msg.Diagnosticstatus.Values(1) = containers.Map("tbc", "tbc");

add(diagnostics_pub_msg.Diagnosticstatus.Values(1),"tbc", "tbc")
end