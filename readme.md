un this command on every new shell you open to have access to the ROS 2 commands:


```bash
source /opt/ros/foxy/setup.bash
```

To buid your package 
Return to the root of your workspace then build your package:


```bash
cd ~/dev_ws
colcon build
```

To see the data being published on a topic:


```bash
ros2 topic echo <topic_name>
```
