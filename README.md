# vrep-ros-control

This repo will allow you to control a quadcopter in VREP through ROS in Python. The current project is using `/quad_cmd_twist` that can be controlled with your keyboard. The current scenario allows the user to roll, pitch and yaw. However, takeoff and land has not been implemented.

#### Requirements

  - ROS Kinetic on Ubuntu 16.04 LTS
  - VREP 3.2.2
  - 'ros' plugin loaded in VREP. If for some reason, you do not see 'ros' plugin when you start vrep or get 'ros' load failed error then follow this tutorial: https://www.youtube.com/watch?v=3Ml0N8-iCwU
  - rospy
  - rospkg

#### Compilation

1. To run the program, first run `roscore` in one terminal and `./vrep.sh` in another terminal. If you see 'ros' plugin succeeded then move to step 2.
2. Start the simulation.
3. In another terminal, run `./main.py` or `python main.py`
4. To control the drone, press w, a, s, d, q, e keys on the keyboard.
5. To stop publishing, press X. This will stop all current nodes.


#### License
MIT
