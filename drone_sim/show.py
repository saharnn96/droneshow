from turtle import pos
import rclpy
from rclpy.node import Node

from operator import index
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil # Needed for command message definitions
import time
import argparse
import glob
import numpy as np

from std_msgs.msg import String

# parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
# parser.add_argument('--connect',
#                     help="Vehicle connection target string. If not specified, SITL automatically started and used.")
# parser.add_argument('--id',
#     help="Vehicle Id")
# parser.add_argument('--time',
#     help="time")
# args = parser.parse_args()

# connection_string = args.connect
# id = args.id
id = 1
# last = args.time

# Start SITL if no connection string specified
# if not connection_string:
# connection_string = '127.0.0.1:14540'

# vehicle = connect(connection_string, wait_ready=False)


# def goto_position_target_local_ned(id, north, east, down, vx, vy, vz, ax, ay, az):
#     """
#     Send SET_POSITION_TARGET_LOCAL_NED command to request the vehicle fly to a specified
#     location in the North, East, Down frame.
#     It is important to remember that in this frame, positive altitudes are entered as negative
#     "Down" values. So if down is "10", this will be 10 metres below the home altitude.
#     Starting from AC3.3 the method respects the frame setting. Prior to that the frame was
#     ignored. For more information see:
#     http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_local_ned
#     See the above link for information on the type_mask (0=enable, 1=ignore).
#     At time of writing, acceleration and yaw bits are ignored.
#     """
#     msg = vehicle.message_factory.set_position_target_local_ned_encode(
#         0,       # time_boot_ms (not used)
#         id, 0,    # target system, target component
#         mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
#         # 0b0000110000000000, # type_mask (only positions enabled)
#         0b0000110111000000,
#         north, east, down, # x, y, z positions (or North, East, Down in the MAV_FRAME_BODY_NED frame
#         vx, vy, vz, # x, y, z velocity in m/s  (not used)
#         ax, ay, az, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
#         0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
#     # send command to vehicle
#     vehicle.send_mavlink(msg)

# def PX4setMode(id, mavMode):
#     vehicle._master.mav.command_long_send(     id, 0,
#                                                mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
#                                                209,
#                                                mavMode, 0, 0, 0, 0, 0)

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.publisher_ = self.create_publisher(String, 'Marker', 10)
        timer_period = 3  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.i += 1
        fps = 3
        f = open(f"rogoz/1fps-10drones/{id}.txt", "r")
        lines = f.readlines()
        # while(time.time_ns() < float(last) + 10e09):
        #     pass
        # PX4setMode(id, 6)
        # vehicle.armed = True
        # while not vehicle.armed:
        #     time.sleep(1)
        # PX4setMode(id, 6)
        # for i in range(100):
        #     goto_position_target_local_ned(id, 0, 0, -0.5, 0, 0, 0 ,0 , 0, 0)
        #     time.sleep(0.01)
        time.sleep(0.4)
        line_counter = self.i
        # for line in lines:
        #     pos0 = [vehicle.location.local_frame.north, vehicle.location.local_frame.east, -vehicle.location.local_frame.down]
        index = line_counter + 15
        if (index + 1) < len(lines):   
            line_elements = lines[index].split()
        # else:
            # continue
        pos1 = [float(line_elements[1]), float(line_elements[2]) - 3 * (float(id) - 1), float(line_elements[3])]
        line_elements = lines[index + 1].split()
        pos2 = [float(line_elements[1]), float(line_elements[2]) - 3 * (float(id) - 1), float(line_elements[3])]
        vel = ((np.array(pos2) - np.array(pos1))/(1/fps)).tolist()
        time.sleep((1/fps))
        last_time = time.time_ns()
        # while(time.time_ns() - last_time < (1/fps)*1e9):
    #         goto_position_target_local_ned(id, pos1[0], pos1[1], -pos1[2], vel[0], vel[1], -vel[2] ,0 , 0, 0)
            # time.sleep(0.01)
        msg = String()
        msg.data = str(pos2)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):        
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()