import time
from adafruit_servokit import ServoKit
from gpiozero import Button, DigitalInputDevice
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
fingergroupPinH=DigitalInputDevice(4,pull_up=True)
fingergroupPinL=DigitalInputDevice(14,pull_up=True)

#index finger is controlled separately
# fingerindexPinH=DigitalInputDevice(17,pull_up=True)
# fingerindexPinL=DigitalInputDevice(18,pull_up=True)
# fingerThumbPinH=DigitalInputDevice(22,pull_up=True)
# fingerThumbPinL=DigitalInputDevice(23,pull_up=True)

#wrist has 3 degrees of freedom, each controlled separately
# wristLeftPinH=DigitalInputDevice(9,pull_up=True)
# wristLeftPinL=DigitalInputDevice(25,pull_up=True)
# wristRightPinH=DigitalInputDevice(11,pull_up=True)
# wristRightPinL=DigitalInputDevice(8 ,pull_up=True)
# wristHorizontalPinH=DigitalInputDevice(6,pull_up=False)
# wristHorizontalPinL=DigitalInputDevice(12,pull_up=False)

elbowPinH=DigitalInputDevice(22,pull_up=True)
elbowPinL=DigitalInputDevice(23,pull_up=True)
time.sleep(1)
while True:
    #move fingers:pinky, ring and middle fingers
    f.setServoThrottleFilter(finger1, fingergroupPinH.value, fingergroupPinL.value,"small")
    f.setServoThrottleFilter(finger2, fingergroupPinH.value, fingergroupPinL.value,"small")
    f.setServoThrottleFilter(finger3, fingergroupPinH.value, fingergroupPinL.value,"small")
    f.setServoThrottleFilter(finger4, fingergroupPinH.value, fingergroupPinL.value,"small")
    f.setServoThrottleFilter(finger5, fingergroupPinH.value, fingergroupPinL.value,"small")

    # f.setServoThrottleFilter(wristLeft, wristLeftPinH.value, wristLeftPinL.value,"large")
    # f.setServoThrottleFilter(wristRight, wristRightPinH.value, wristRightPinL.value,"large")
    # f.setServoThrottleFilter(wristHorizontal, wristHorizontalPinH.value, wristHorizontalPinL.value,"large")
    f.setServoThrottleFilter(elbow, elbowPinH.value, elbowPinL.value,"large")
    if elbowPinH.value != 0 or elbowPinL.value != 0:
        print("elbowPinH: " + str(elbowPinH.value) + " elbowPinL: " + str(elbowPinL.value))