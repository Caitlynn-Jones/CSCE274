#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped
from time import sleep

def talker():
    pub = rospy.Publisher('car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)
    rospy.init_node('square', anonymous=True)
    rate = rospy.Rate(10)

    msg = Twist2DStamped(header=None, v=0.4, omega=1.2)
    pub.publish(msg)
    sleep(2)
    msg = Twist2DStamped(header=None, v=0.0, omega=0.0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0.1, omega=8.0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0.0, omega=0.0)
    pub.publish(msg)
    sleep(1)

    msg = Twist2DStamped(header=None, v=0.4, omega=1.2)
    pub.publish(msg)
    sleep(2)
    msg = Twist2DStamped(header=None, v=0.0, omega=0.0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0.1, omega=8.0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0.0, omega=0.0)
    pub.publish(msg)
    sleep(1)

    msg = Twist2DStamped(header=None, v=0.4, omega=1.2)
    pub.publish(msg)
    sleep(2)
    msg = Twist2DStamped(header=None, v=0.0, omega=0.0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0.1, omega=8.0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0.0, omega=0.0)
    pub.publish(msg)
    sleep(1)

    msg = Twist2DStamped(header=None, v=0.4, omega=1.2)
    pub.publish(msg)
    sleep(2)
    msg= Twist2DStamped(header=None, v=0.0, omega=0.0)
    pub.publish(msg)
    sleep(1)
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
