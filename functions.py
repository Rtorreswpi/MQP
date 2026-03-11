import time
from adafruit_servokit import ServoKit
from gpiozero import MCP3008, DigitalInputDevice


def setServoThrottleFilter(servo, pin1, pin2,servoType):
    """Sets the throttle of a servo based on the state of two pins"""
    if pin1 == True and pin2 == False:
        servo.throttle = 1
    elif pin1 == False and pin2 == True:
        servo.throttle = -1
    else:#large servos need a small amount of throttle to hold position, small servos can be stopped completely
        if servoType == "large":
            servo.throttle = 0.1
        else:
            servo.throttle = 0
