
(cl:in-package :asdf)

(defsystem "sam_custom_messages-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :diagnostic_msgs-msg
               :geometry_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Object" :depends-on ("_package_Object"))
    (:file "_package_Object" :depends-on ("_package"))
    (:file "capability" :depends-on ("_package_capability"))
    (:file "_package_capability" :depends-on ("_package"))
    (:file "current_action" :depends-on ("_package_current_action"))
    (:file "_package_current_action" :depends-on ("_package"))
    (:file "diagnostics" :depends-on ("_package_diagnostics"))
    (:file "_package_diagnostics" :depends-on ("_package"))
    (:file "hand_pos" :depends-on ("_package_hand_pos"))
    (:file "_package_hand_pos" :depends-on ("_package"))
    (:file "object_state" :depends-on ("_package_object_state"))
    (:file "_package_object_state" :depends-on ("_package"))
    (:file "robot_state" :depends-on ("_package_robot_state"))
    (:file "_package_robot_state" :depends-on ("_package"))
    (:file "user_prediction" :depends-on ("_package_user_prediction"))
    (:file "_package_user_prediction" :depends-on ("_package"))
  ))