#!/usr/bin/env python
##########################################################################################
#                                                                                        #
#                      simple code to control basic flying states                        #
#                               using Copter Class                                       #
#                                                                                        #
#   Brief explaination of the Class                                                      #
#                                                                                        #
#       The Class has Two parts :                                                        #
#                                                                                        #
#           1. Setting up the Copter's Attributes                                        #
#           2. Publishing the Attributes so that it may fly according to your will       #
#                                                                                        #
#              1. Setting up the Copter's Attributes                                     #
#                                                                                        #
#                   Multiple Functions can be used in order to control the Copter        #
#                                                                                        #
#                      Basic Setters                                                     #
#                           - Change X and Y velocities                                  #
#                           - Change Height ( Global Prespective )                       #
#                           - Change the angle continously at constant speed             #
#                                                                                        #
#                       Basic Accelerators & Decelerators                                #
#                           - Change X and Y velocities at specific Rate                 #
#                           - Change Height ( Self Prespective )                         #
#                                                                                        #
#                                                                                        #
#                       Basic Turn at specific angle                                     #
#                           - Turn Right & Left at Specific Angle                        #
#                                                                                        #
#                       Stop all Workings and Stay Still                                 #
#                                                                                        #
#                       User Controller                                                  #
#                                                                                        #
#                           - Q or 7	to      turn Left                                #
#                           - E or 9	to      turn Right                               #
#                           - W or 8	to      Move forward                             #
#                           - A or 4	to      Move Left                                #
#                           - S or 2	to      Move Backward                            #
#                           - D or 6	to      Move Right                               #
#                           - + 	    to      Accend                                   #
#                           - - 	    to      Decend                                   #
#                           - X or 5	to      Stop                                     #
#                                                                                        #
#              2. Publishing the current settings                                        #
#                                                                                        #
#
##########################################################################################
import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


class Copter:

    # Attributes
    publisher = 0
    dimentions = Twist()

    velocityX = 0.0
    velocityY = 0.0
    height = 0.0

    angularZ = 0.0

    # Intializer / Constructor
    def __init__(self):
        self.publisher = rospy.Publisher('/quad_cmd_twist', Twist, queue_size=100)
        rospy.init_node('vrep', anonymous=True)

    # Basic Setters
    def changeVelocityX(self, value):
        self.velocityX = value
    def changeVelocityY(self, value):
        self.velocityY = value
    def changeHeightZ(self, value):
        self.height = value
    def changeAngular(self, value):
        self.angularZ = value

    # Basic Accelerator & Decelerator
    def accelerateAxisX(self, value):
        self.velocityX = self.velocityX + value
    def accelerateAxisY(self, value):
        self.velocityY = self.velocityY + value
    def decelerateAxisX(self, value):
        self.velocityX = self.velocityX - value
    def decelerateAxisY(self, value):
        self.velocityY = self.velocityY - value
    def accend(self,value):
        self.height = self.height + value
    def decend(self, value):
        self.height = self.height - value

    # Change Rotation
    def turnRight(self,value):
        self.changeAngular(-1.0)
        self.PublishPresentStates()
        value = 1 / value
        rate = rospy.Rate(value)
        rate.sleep()
        self.stop()
        self.PublishPresentStates()

    def turnLeft(self,value):
        self.changeAngular(1.0)
        self.PublishPresentStates()
        value = 1 / value
        rate = rospy.Rate(value)
        rate.sleep()
        self.stop()
        self.PublishPresentStates()

    # Stop In All Directions And Ways
    def stop(self):
        self.changeVelocityX(0.0)
        self.changeVelocityY(0.0)
        self.changeHeightZ(0.0)
        self.changeAngular(0.0)

    # Publishing All Attributes To ROS For V-REP
    def PublishPresentStates(self):
        self.dimentions.linear.x = self.velocityX
        self.dimentions.linear.y = self.velocityY
        self.dimentions.linear.z = self.height
        self.dimentions.angular.x = 0
        self.dimentions.angular.y = 0
        self.dimentions.angular.z = self.angularZ
        self.publisher.publish(self.dimentions)

    # Controller For Users To Control and Check the Movements
    def keysCheck(self,key,value):
        if key == 'w' or key == '8':
            self.velocityX = value
        if key == 's'or key == '2':
            self.velocityX = -1*value
        if key == 'd'or key == '6':
            self.velocityY = -1*value
        if key == 'a'or key == '4':
            self.velocityY = value
        if key == 'x'or key == '5':
            self.stop()
        if key == 'q'or key == '7':
            self.turnLeft(value)
        if key == 'e'or key == '9':
            self.turnRight(value)
        if key == '+':
            self.accend(value)
        if key == '-':
            self.decend(value)

    def controller(self,key,value):
        while(key != 'z'):
            key = input("enter key (only small alphabets) : ")
            self.keysCheck(key,value)
            self.PublishPresentStates()
        return key

    # A Sleep Function for Simulation Ease
    def copter_Sleep(self,value):
    	self.rate = rospy.Rate(value)
    	self.rate.sleep()


def menu():
	quadcopter = Copter()
	key = quadcopter.controller('w',0.3)

if __name__ == '__main__':
    try:
        menu()
    except rospy.ROSInterruptException:
        pass
