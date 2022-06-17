from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='drone_sim',
            namespace='visualization_msgs1',
            executable='show',
            name='msg'
        ),
        Node(
            package='drone_sim',
            namespace='visualization_msgs2',
            executable='show',
            name='msg'
        )
    ])