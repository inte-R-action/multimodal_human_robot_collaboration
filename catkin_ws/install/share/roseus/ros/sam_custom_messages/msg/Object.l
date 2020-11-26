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
  :slots (_Id _Type _Info ))

(defmethod sam_custom_messages::Object
  (:init
   (&key
    ((:Id __Id) 0)
    ((:Type __Type) 0)
    ((:Info __Info) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _Id (round __Id))
   (setq _Type (round __Type))
   (setq _Info __Info)
   self)
  (:Id
   (&optional __Id)
   (if __Id (setq _Id __Id)) _Id)
  (:Type
   (&optional __Type)
   (if __Type (setq _Type __Type)) _Type)
  (:Info
   (&optional __Info)
   (if __Info (setq _Info __Info)) _Info)
  (:serialization-length
   ()
   (+
    ;; int8 _Id
    1
    ;; int8 _Type
    1
    ;; string[] _Info
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _Info)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _Id
       (write-byte _Id s)
     ;; int8 _Type
       (write-byte _Type s)
     ;; string[] _Info
     (write-long (length _Info) s)
     (dolist (elem _Info)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _Id
     (setq _Id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _Id 127) (setq _Id (- _Id 256)))
   ;; int8 _Type
     (setq _Type (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _Type 127) (setq _Type (- _Type 256)))
   ;; string[] _Info
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _Info (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _Info i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get sam_custom_messages::Object :md5sum-) "08793d2cad4a594af24da817df20da39")
(setf (get sam_custom_messages::Object :datatype-) "sam_custom_messages/Object")
(setf (get sam_custom_messages::Object :definition-)
      "# Message containg information on objects within environment
#
# Unique ID of object
int8 Id
#
# Type of object ID
int8 Type
#
# Additional information on object
string[] Info
")



(provide :sam_custom_messages/Object "08793d2cad4a594af24da817df20da39")


