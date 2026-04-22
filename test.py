import time
from adafruit_servokit import ServoKit
from gpiozero import Button, DigitalInputDevice
from signal import pause
import functions as f
kit = ServoKit(channels=16)
pinA6 = DigitalInputDevice(4, pull_up=True)
pinA7 = DigitalInputDevice(14, pull_up=True)
finger1=kit.continuous_servo[0]#pinky
finger1.throttle=0.1
while True:
    finger1.throttle=1
    time.sleep(1)
    finger1.throttle=-1
    time.sleep(1)
    finger1.throttle=0.1
    time.sleep(1)