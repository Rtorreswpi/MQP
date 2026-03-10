import time
from adafruit_servokit import ServoKit
from gpiozero import MCP3008, DigitalInputDevice, Button
from signal import pause
import functions as f
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
#finger servos
finger1=kit.continuous_servo[0]
finger1.throttle=0
finger2=kit.continuous_servo[1]
finger2.throttle=0
finger3=kit.continuous_servo[2]
finger3.throttle=0
finger4=kit.continuous_servo[3]
finger4.throttle=0
finger5=kit.continuous_servo[4]
finger5.throttle=0
#wrist servos
wristRight=kit.continuous_servo[5]
wristRight.throttle=0
wristLeft=kit.continuous_servo[6]
wristLeft.throttle=0
wristHorizontal=kit.continuous_servo[7]
wristHorizontal.throttle=0
#elbow servo
elbow=kit.continuous_servo[8]
elbow.throttle=0

Sstop=0
Bstop=0.1
#Set pins for servo control
finger1PinH=Button(7,pull_up=False)
finger1PinL=Button(8,pull_up=False)
finger2PinH=Button(11,pull_up=False)
finger2PinL=Button(12,pull_up=False)
finger3PinH=Button(15,pull_up=False)
finger3PinL=Button(16,pull_up=False)
finger4PinH=Button(21,pull_up=False)
finger4PinL=Button(22,pull_up=False)
finger5PinH=Button(23,pull_up=False)
finger5PinL=Button(24,pull_up=False)
wristLeftPinH=Button(31,pull_up=False)
wristLeftPinL=Button(32,pull_up=False)
wristRightPinH=Button(35,pull_up=False)
wristRightPinL=Button(36,pull_up=False)
wristHorizontalPinH=Button(37,pull_up=False)
wristHorizontalPinL=Button(38,pull_up=False)
elbowPinH=Button(26,pull_up=False)
elbowPinL=Button(29,pull_up=False)
time.sleep(1)
while True:
    f.setServoThrottleFilter(finger1, finger1PinH.is_pressed, finger1PinL.is_pressed,"small")
    f.setServoThrottleFilter(finger2, finger2PinH.is_pressed, finger2PinL.is_pressed,"small")
    f.setServoThrottleFilter(finger3, finger3PinH.is_pressed, finger3PinL.is_pressed,"small")
    f.setServoThrottleFilter(finger4, finger4PinH.is_pressed, finger4PinL.is_pressed,"small")
    f.setServoThrottleFilter(finger5, finger5PinH.is_pressed, finger5PinL.is_pressed,"small")
    f.setServoThrottleFilter(wristLeft, wristLeftPinH.is_pressed, wristLeftPinL.is_pressed,"large")
    f.setServoThrottleFilter(wristRight, wristRightPinH.is_pressed, wristRightPinL.is_pressed,"large")
    f.setServoThrottleFilter(wristHorizontal, wristHorizontalPinH.is_pressed, wristHorizontalPinL.is_pressed,"large")
    f.setServoThrottleFilter(elbow, elbowPinH.is_pressed, elbowPinL.is_pressed,"large")