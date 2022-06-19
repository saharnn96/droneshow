from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    pkg_name = 'drone_sim'
    pkg_dir = os.popen('/bin/bash -c "source /usr/share/colcon_cd/function/colcon_cd.sh && \
        colcon_cd %s && pwd"' % pkg_name).read().strip()
    return LaunchDescription([    
        Node(
            package='drone_sim',
            namespace='visualization_msgs1',
            executable='show',
            name='msg',
            arguments=['--connect','127.0.0.1:14540' ,'--id','1','--time','$value']
        ),
        # Node(
        #     package='drone_sim',
        #     namespace='visualization_msgs2',
        #     executable='show',
        #     name='msg'
        # ),
        # Node(
        #     package='drone_sim',
        #     namespace='visualization_msgs3',
        #     executable='show',
        #     name='msg'
        # ),
        Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', [os.path.join(pkg_dir, 'config', 'config_file.rviz')]]
        )
    ])