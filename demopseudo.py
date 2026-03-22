import time
from adafruit_servokit import ServoKit
from gpiozero import Button
from signal import pause
import functions as f
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
#finger servos
finger1=kit.continuous_servo[0]#pinky
finger1.throttle=0
finger2=kit.continuous_servo[1]#ring
finger2.throttle=0
finger3=kit.continuous_servo[2]#middle
finger3.throttle=0
finger4=kit.continuous_servo[3]#pointer
finger4.throttle=0
finger5=kit.continuous_servo[4]#thumb
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

#Set pins for servo control
#middle,ring and pinky fingers are controlled together
fingergroupPinH=Button(4,pull_up=False)
fingergroupPinL=Button(14,pull_up=False)
#index finger is controlled separately
fingerindexPinH=Button(17,pull_up=False)
fingerindexPinL=Button(18,pull_up=False)
fingerThumbPinH=Button(22,pull_up=False)
fingerThumbPinL=Button(23,pull_up=False)
#wrist has 3 degrees of freedom, each controlled separately
wristLeftPinH=Button(9,pull_up=False)
wristLeftPinL=Button(25,pull_up=False)
wristRightPinH=Button(11,pull_up=False)
wristRightPinL=Button(8 ,pull_up=False)
wristHorizontalPinH=Button(6,pull_up=False)
wristHorizontalPinL=Button(12,pull_up=False)

elbowPinH=Button(19,pull_up=False)
elbowPinL=Button(16,pull_up=False)
time.sleep(1)
while True:
    #move fingers:pinky, ring and middle fingers
    f.setServoThrottleFilter(finger1, fingergroupPinH.is_pressed, fingergroupPinL.is_pressed,"small")
    f.setServoThrottleFilter(finger2, fingergroupPinH.is_pressed, fingergroupPinL.is_pressed,"small")
    f.setServoThrottleFilter(finger3, fingergroupPinH.is_pressed, fingergroupPinL.is_pressed,"small")
    #move fingers: index and thumb fingers
    f.setServoThrottleFilter(finger4, fingerindexPinH.is_pressed, fingerindexPinL.is_pressed,"small")
    f.setServoThrottleFilter(finger5, fingerThumbPinH.is_pressed, fingerThumbPinL.is_pressed,"small")

    f.setServoThrottleFilter(wristLeft, wristLeftPinH.is_pressed, wristLeftPinL.is_pressed,"large")
    f.setServoThrottleFilter(wristRight, wristRightPinH.is_pressed, wristRightPinL.is_pressed,"large")
    f.setServoThrottleFilter(wristHorizontal, wristHorizontalPinH.is_pressed, wristHorizontalPinL.is_pressed,"large")
    f.setServoThrottleFilter(elbow, elbowPinH.is_pressed, elbowPinL.is_pressed,"large")