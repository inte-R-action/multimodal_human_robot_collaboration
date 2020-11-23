;; Auto-generated. Do not edit!


(when (boundp 'sam_custom_messages::Object)
  (if (not (find-package "SAM_CUSTOM_MESSAGES"))
    (make-package "SAM_CUSTOM_MESSAGES"))
  (shadow 'Object (find-package "SAM_CUSTOM_MESSAGES")))
(unless (find-package "SAM_CUSTOM_MESSAGES::OBJECT")
  (make-package "SAM_CUSTOM_MESSAGES::OBJECT"))

(in-package "ROS")
;;//! \htmlinclude Object.msg.html


(defclass sam_custom_messages::Object
  :super ros::object
  :slots (_id _type _info ))

(defmethod sam_custom_messages::Object
  (:init
   (&key
    ((:id __id) 0)
    ((:type __type) 0)
    ((:info __info) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _type (round __type))
   (setq _info __info)
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:info
   (&optional __info)
   (if __info (setq _info __info)) _info)
  (:serialization-length
   ()
   (+
    ;; int8 _id
    1
    ;; int8 _type
    1
    ;; string[] _info
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _info)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _id
       (write-byte _id s)
     ;; int8 _type
       (write-byte _type s)
     ;; string[] _info
     (write-long (length _info) s)
     (dolist (elem _info)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _id
     (setq _id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _id 127) (setq _id (- _id 256)))
   ;; int8 _type
     (setq _type (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _type 127) (setq _type (- _type 256)))
   ;; string[] _info
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _info (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _info i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get sam_custom_messages::Object :md5sum-) "cc95ebc586991f7be21fb0175298a82c")
(setf (get sam_custom_messages::Object :datatype-) "sam_custom_messages/Object")
(setf (get sam_custom_messages::Object :definition-)
      "# Message containg information on objects within environment
#
# Unique ID of object
int8 id
#
# Type of object ID
int8 type
#
# Additional information on object
string[] info
")



(provide :sam_custom_messages/Object "cc95ebc586991f7be21fb0175298a82c")


