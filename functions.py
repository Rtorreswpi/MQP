import time
from adafruit_servokit import ServoKit
from gpiozero import MCP3008, DigitalInputDevice


def setServoThrottleFilter(servo, pin1, pin2,servoType):
    """Sets the throttle of a servo based on the state of two pins"""
    if pin1 == 1 and pin2 == 0:
        servo.throttle = 1
        # print("moving servo: " + str(servo) + " forward")
    elif pin1 == 0 and pin2 == 1:
        # print("moving servo: " + str(servo) + " backward")
        servo.throttle = -1
    else:#large servos need a small amount of throttle to hold position, small servos can be stopped completely
        # if servo.throttle != 0 and servo.throttle != 0.1:
            # print("stopping servo: " + str(servo))
        if servoType == "large":
            servo.throttle = 0.1
        else:
            servo.throttle = 0
