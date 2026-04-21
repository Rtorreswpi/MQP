import time
from adafruit_servokit import ServoKit
from gpiozero import Button, DigitalInputDevice
from signal import pause
import functions as f

pinA6 = DigitalInputDevice(4, pull_up=True)
pinA7 = DigitalInputDevice(14, pull_up=True)
finger1=kit.continuous_servo[0]#pinky
finger1.throttle=0
finger2=kit.continuous_servo[1]#ring
finger2.throttle=0
while True:
    finger1.throttle=1
    time.sleep(0.5)
    finger1.throttle=-1
    time.sleep(0.5)
    finger1.throttle=0
    time.sleep(0.5)