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
        ),
        Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            # arguments=['-d', [os.path.join(pkg_dir, 'config', 'config_file.rviz')]]
        )
    ])