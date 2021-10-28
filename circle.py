#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped
from time import sleep
#v = 0.0
#omega = 0.0

def talker():
    pub = rospy.Publisher('car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)
    rospy.init_node('circle', anonymous=True)
    rate = rospy.Rate(10)

    msg = Twist2DStamped(header=None, v=0.25, omega=-3.80)
    pub.publish(msg)
    sleep(8)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
