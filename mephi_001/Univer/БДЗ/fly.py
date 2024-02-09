"""Облет точек по заданным координатам и запись их высот
Войтов Сергей Б22-211"""

import rospy
from clover import srv
from sensor_msgs.msg import Range

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)

initial_flight_params = {'x': 0, 'y': 0, 'z': 1.5, 'frame_id': 'body', 'auto_arm': True}

navigate(**initial_flight_params)
rospy.sleep(3)


def navigate_wait(x, y, z, frame_id="aruco_map"):
    navigate(x=x, y=y, z=z, frame_id=frame_id)
    rospy.sleep(10)


# список точек для проверки
points = [(1.25, 1), (0.5, 2.7), (-1, -2), (2, -1), (0, 0), (3, 3), (-2, 2), (-3, -3), (1, -3), (-1, 1)]

heights_dict = {}  # словарь высот

for point in points:
    navigate_wait(point[0], point[1], 1.5)
    range_message = rospy.wait_for_message("/rangefinder/range", Range)
    current_height = range_message.range

    heights_dict[point] = current_height

for point, height in heights_dict.items():
    print(f"Point: {point}, Height: {height}")
