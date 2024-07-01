#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16
left_encoder_ticks = 0
def talker():
    global left_encoder_ticks
    pub = rospy.Publisher("/left_ticks", Int16, queue_size=1)
    rospy.init_node('left_encoder_ticks', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():       
        rospy.loginfo(left_encoder_ticks)
        pub.publish(left_encoder_ticks)
        left_encoder_ticks = left_encoder_ticks + 1
        rate.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass




