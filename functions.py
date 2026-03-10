import time
from adafruit_servokit import ServoKit
from gpiozero import MCP3008, DigitalInputDevice


def setServoThrottleFilter(servo, pin1, pin2,servoType):
    if pin1 == True and pin2 == False:
        servo.throttle = 1
    elif pin1 == False and pin2 == True:
        servo.throttle = -1
    else:
        if servoType == "large":
            servo.throttle = 0.1
        else:
            servo.throttle = 0
