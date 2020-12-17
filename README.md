# multimodal_human_robot_collaboration

Project for human-robot collaboration in an industrial manufacturing environment. Development of Synthetic Autobiographical Memory (SAM) system for use in manufacturing tasks when working woth a robotic arm forr natural human interaction by predicting future needs.

ROS implementation for use on a UR3 robot using Shimmer IMUs, Optitrack motion capture and RGBD cameras to recognise positions, actions and object states.

ROS >= melodic

postgresql: https://www.postgresql.org/download/

pgadmin 4: https://www.pgadmin.org/download/

Python libraries required:

  pyserial: python3 -m pip install pyserial

  matplotlib: python3 -m pip install -U matplotlib

  sklearn: pip3 install scikit-learn

  libbluetooth-dev: sudo apt-get install -y libbluetooth-dev

  pybluez: pip3 install pybluez (this requires ^ to be installed first!)

  rospkg: pip3 install -U rospkg

  psycopg2: pip3 install psycopg2
