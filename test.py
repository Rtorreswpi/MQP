import time
from adafruit_servokit import ServoKit
from gpiozero import Button, DigitalInputDevice
from signal import pause
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
wristRight.throttle=0.1
wristLeft=kit.continuous_servo[6]
wristLeft.throttle=0.1
wristHorizontal=kit.continuous_servo[7]
wristHorizontal.throttle=0.1
#elbow servo
elbow=kit.continuous_servo[8]
elbow.throttle=0.1
throttleHigh=0.5
throttleLow=-0.5
kit = ServoKit(channels=16)
while True:
    finger1.throttle=throttleHigh
    time.sleep(1)
    finger1.throttle=throttleLow
    time.sleep(1)


    # finger1.throttle=throttleHigh
    # time.sleep(0.2)
    # finger1.throttle=throttleHigh
    # finger2.throttle=throttleHigh
    # time.sleep(0.2)
    # finger1.throttle=throttleHigh
    # finger2.throttle=throttleHigh
    # finger3.throttle=throttleHigh
    # time.sleep(0.2)
    # finger1.throttle=throttleHigh
    # finger2.throttle=throttleHigh
    # finger3.throttle=throttleHigh
    # finger4.throttle=throttleHigh
    # time.sleep(0.2)
    # finger1.throttle=throttleHigh
    # finger2.throttle=throttleHigh  
    # finger3.throttle=throttleHigh
    # finger4.throttle=throttleHigh
    # finger5.throttle=throttleHigh
    # time.sleep(0.2)
    # finger1.throttle=0
    # finger2.throttle=throttleHigh
    # finger3.throttle=throttleHigh
    # finger4.throttle=throttleHigh
    # finger5.throttle=throttleHigh
    # time.sleep(0.2)
    # finger2.throttle=0
    # finger3.throttle=throttleHigh
    # finger4.throttle=throttleHigh
    # finger5.throttle=throttleHigh
    # time.sleep(0.2)
    # finger3.throttle=0
    # finger4.throttle=throttleHigh
    # finger5.throttle=throttleHigh
    # time.sleep(0.2)
    # finger4.throttle=0
    # finger5.throttle=throttleHigh
    # time.sleep(0.2)
    # finger5.throttle=0
    # time.sleep(1)
    # finger1.throttle=throttleLow
    # time.sleep(0.2)
    # finger1.throttle=throttleLow
    # finger2.throttle=throttleLow
    # time.sleep(0.2)
    # finger1.throttle=throttleLow
    # finger2.throttle=throttleLow
    # finger3.throttle=throttleLow
    # time.sleep(0.2)
    # finger1.throttle=throttleLow
    # finger2.throttle=throttleLow
    # finger3.throttle=throttleLow
    # finger4.throttle=throttleLow
    # time.sleep(0.2)
    # finger1.throttle=throttleLow
    # finger2.throttle=throttleLow
    # finger3.throttle=throttleLow
    # finger4.throttle=throttleLow
    # finger5.throttle=throttleLow
    # time.sleep(0.2)
    # finger1.throttle=0
    # finger2.throttle=throttleLow
    # finger3.throttle=throttleLow
    # finger4.throttle=throttleLow
    # finger5.throttle=throttleLow
    # time.sleep(0.2)
    # finger2.throttle=0
    # finger3.throttle=throttleLow
    # finger4.throttle=throttleLow
    # finger5.throttle=throttleLow
    # time.sleep(0.2)
    # finger3.throttle=0
    # finger4.throttle=throttleLow
    # finger5.throttle=throttleLow
    # time.sleep(0.2)
    # finger4.throttle=0
    # finger5.throttle=throttleLow
    # time.sleep(0.2)
    # finger5.throttle=0
    # time.sleep(1)