#!/usr/bin/env python
# Execute as a python script
# Description: Set linear and angular values for the Turtle.
# Name: Chase Deets (chd5hq)

import rospy				# Needed to create a ROS node -Python client library
# Message type that Turtlesim accepts - usually via the topic cmd_vel
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty
import random
from math import pi,pow,atan2,sqrt

xpos = None
ypos = None
thet = None


def fncallback(pos):
    global xpos,ypos,thet
    xpos = pos.x
    ypos = pos.y
    thet = pos.theta

class ControlTurtlesim():

    def __init__(self):
        # self represents the instance of the class.
        # By using the "self" keyword we can access the attributes
        # and methods of the class in python.
        # "__init__" is a reseved method in python classes.
        # It is known as a constructor in object oriented concepts.
        # This method called when an object is created from the class
        # and it allows the class to initialize the attributes of the class.


        rospy.init_node('ControlTurtlesim', anonymous=False)
        # ControlTurtlesim is the name of the node sent to the master
        # You can only have one node in a rospy process,
        # so you can only call rospy.init_node() once!

        # The anonymous argument: The anonymous keyword argument is mainly used for nodes
        # where you normally expect many of them to be running and don't care
        # about their names (e.g. tools, GUIs).
        # It adds a random number to the end of your node's name,
        # to make it unique. Unique names are more important for nodes
        # like drivers, where it is an error if more than one is running.
        # If two nodes with the same name are detected on a ROS graph,
        # the older node is shutdown.

		# Message to screen
        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")
        linVel = 1
        angVel = 0
        sideLen = input("Length of side: ")


        # Keys CTRL + c will stop this script
        rospy.on_shutdown(self.shutdown)

	    # Since we want to move the turtle, this node will pubish a
        # Twist message on topic /turtle1/cmd_vel. lets do that below-
        self.position = rospy.Subscriber('/turtle1/pose', Pose, fncallback)
        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        # Here we are creating a handle to publish messages to a topic using
        # the rospy.Publisher class.
        # The most common usage for this is to provide the name of the topic
        # and the message class/type of the topic.
        # You can then call publish() on that handle to publish a message.
        # General usage:
        # pub = rospy.Publisher('topic_name', message class, queue_size=10)


	    # Turtlesim will receive our messages 10 times per second.
        rate = rospy.Rate(20);
        # Do not confuse this 10 with the queue_size = 10 above.
	    # 10 Hz is fine as long as the processing does not exceed
        #   1/10 second.

        rospy.loginfo("Set rate 20Hz")

        # We may want the user to specify the rate rather than echo a fixed rate.

        # Twist is geometry_msgs for linear and angular velocity
        # create an object of the class Twist.
        move_cmd = Twist()

	    # Linear speed in x in units/second: positive values imply forward,
        # negative values == backwards
        move_cmd.linear.x = linVel	# Modify this value to change the Turtle's speed

        # Turn at 0 radians/s
        move_cmd.angular.z = angVel
        # Modify this value to cause rotation rad/s

        #spawn turtle at a random location:
        rospy.wait_for_service('turtle1/teleport_absolute')
        turtle1_teleport_absolute = rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
        turtle1_teleport_absolute(1,1,0) #sets it to (1,1)

        #clear background after teleport and set to red

        rospy.set_param('/background_b',0)
        rospy.set_param('/background_r',250)
        rospy.set_param('/background_g',0)

        clean_slate = rospy.ServiceProxy('clear', Empty)
        clean_slate()



        xin, yin, tin = 0, 0, 0


        rate.sleep()
        rate.sleep()
        xin = round(xpos,2)
        yin = round(ypos,2)
        tin = round(thet,1)

        print("Center at:", xin, " ", yin)
	    # Loop until you type CTRL+c
        #while not rospy.is_shutdown():
	         # publish Twist values to the Turtlesim node /cmd_vel
             # handle.publish(message class instance)
        while (xpos < 1+sideLen) and not rospy.is_shutdown():
            self.cmd_vel.publish(move_cmd)
            #rate.sleep()
        #turn in place
        turtle1_teleport_absolute(xpos,ypos,pi/2)

        while(ypos < 1+sideLen and not rospy.is_shutdown()):
            self.cmd_vel.publish(move_cmd)
            #rate.sleep()

        turtle1_teleport_absolute(xpos,ypos,pi)

        while(xpos > 1 and not rospy.is_shutdown()):
            self.cmd_vel.publish(move_cmd)
            #rate.sleep()

        turtle1_teleport_absolute(xpos,ypos,-pi/2)

        while(ypos > 1 and not rospy.is_shutdown()):
            #print(ypos)
            self.cmd_vel.publish(move_cmd)
            rate.sleep

            #debug:
            #print("xpos:", round(xpos,4), " ypos:", round(ypos,4)," theta:", thet)

	        # wait for 0.1 seconds (10 HZ) and publish again
        rate.sleep()


    def shutdown(self):
        # You can stop turtlesim_move by publishing an empty Twist message
        rospy.loginfo("Stopping the turtle")

        self.cmd_vel.publish(Twist())

        # Give it some time to stop
        rospy.sleep(1)

if __name__ == '__main__':
    # Try and Except.
    # If an error is encountered, a try block code execution is stopped and
    # transferred down to the except block.

    try:
        ControlTurtlesim()
    except:
        rospy.loginfo("End of the swim for this Turtle.")
