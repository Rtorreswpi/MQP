import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=8)
kit.continuous_servo[0].throttle=0
kit.continuous_servo[1].throttle=0
throt=0
time.sleep(1)
while True:
    dir=input("pick a direction(l or r): ")
    if dir == "l": throt=-1
    elif dir =="r":throt=1
    else:
        print("incorrect direction try again")
        throt=0
    kit.continuous_servo[1].throttle = throt