# multimodal_human_robot_collaboration

Project for human-robot collaboration in an industrial manufacturing environment. Development of cognitive architecture for use in manufacturing tasks when working with a robotic arm for natural human interaction by predicting future needs.

ROS implementation for use on a UR3 robot with action recognition with LSTM based future prediction for adaptive robot action planning.

Human Action Recognition performed using Shimmer IMUs and Kinect skeleton tracking. Four assembly actions and six control gestures recognised.
RealSense D435i vision recognition for tracking the number of fasteners assembled.
Tools status sensor recognises if tool currently in use of not.

LSTM based future prediction tracks staus of assembly using task knowedge, prerequisites and action probabilities. Robot autonomously plans actions to synchronise with user.

## Associated publications:

Male, J. and Martinez-Hernandez, U., “Deep learning based robot cognitive architecture for collaborative assembly tasks,” Robotics and Computer-Integrated Manufacturing (RCIM), 2023 (accepted for publication)

Male, J. and Martinez-Hernandez, U., “Dataset for Deep learning based robot cognitive architecture for collaborative assembly tasks,” Bath: University of Bath Research Data Archive. 2023. Available from: https://doi.org/10.15125/BATH-01161.

Male, J., Al, G.A, Shabani, A., and Martinez-Hernandez, U., “Multimodal sensorbased human-robot collaboration in assembly tasks,” 2022 IEEE International Conference on Systems, Man, and Cybernetics (SMC), Prague, Czech Republic, 2022, pp. 1266-1271

Male, J. and Martinez-Hernandez, U., “Collaborative architecture for human-robot assembly tasks using multimodal sensors,” 2021 20th International Conference on Advanced Robotics (ICAR), Ljubljana, Slovenia, 2021, pp. 1024-1029

## Requirements overview:

ROS >= melodic

postgresql: https://www.postgresql.org/download/

pgadmin 4: https://www.pgadmin.org/download/

Python version 3-3.7 required, >=3.8 will not work

Python libraries required:

  pyserial: python3 -m pip install pyserial

  matplotlib: python3 -m pip install -U matplotlib

  sklearn: pip3 install scikit-learn

  libbluetooth-dev: sudo apt-get install -y libbluetooth-dev

  pybluez: pip3 install pybluez (this requires ^ to be installed first!)

  rospkg: pip3 install -U rospkg

  psycopg2: pip3 install psycopg2
