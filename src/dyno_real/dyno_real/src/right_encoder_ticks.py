#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16
right_encoder_ticks = 0
def talker():
    global right_encoder_ticks
    pub = rospy.Publisher("/right_ticks", Int16, queue_size=1)
    rospy.init_node('right_encoder_ticks', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():       
        rospy.loginfo(right_encoder_ticks)
        pub.publish(right_encoder_ticks)
        right_encoder_ticks = right_encoder_ticks + 1
        rate.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass




