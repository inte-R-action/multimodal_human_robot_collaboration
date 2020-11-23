function natnet_event_callback( ~ , evnt )
global object_state_pub object_pub_msg model hand_state_pub hand_pub_msg latest_evnt

% the input argument, evnt, is a c structure half converted into a
% matlab structure.
latest_evnt = evnt.data;

if ( model.RigidBodyCount > 0 )
    for i = 1:model.RigidBodyCount
        if contains(model.RigidBody(i).Name, 'hand','IgnoreCase',true)
            recv_hand(model.RigidBody(i).Name, latest_evnt.RigidBodies(i), latest_evnt.iFrame, latest_evnt.fTimestamp)
            send(hand_state_pub, hand_pub_msg)
        else
            recv_rigidbody(model.RigidBody(i).Name, latest_evnt.RigidBodies(i), latest_evnt.iFrame, latest_evnt.fTimestamp)
            send(object_state_pub, object_pub_msg)
        end
        
    end
    
end

pause(2)

end

