import time
from adafruit_servokit import ServoKit
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
#finger servos
kit.continuous_servo[0].throttle=0
kit.continuous_servo[1].throttle=0
kit.continuous_servo[2].throttle=0
kit.continuous_servo[3].throttle=0
kit.continuous_servo[4].throttle=0
#wrist servos
kit.continuous_servo[5].throttle=0
kit.continuous_servo[6].throttle=0
kit.continuous_servo[7].throttle=0
#elbow servo
kit.continuous_servo[8].throttle=0

Sstop=0
Bstop=0.1
time.sleep(1)
while True:
    
    if dir == "l": throt=-1
    elif dir =="r":throt=1
    else:
        print("incorrect direction try again")
        throt=0
    kit.continuous_servo[1].throttle = throt