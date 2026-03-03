import time
from adafruit_servokit import ServoKit
from gpiozero import MCP3008, DigitalInputDevice
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
#finger servos
finger1=kit.continuous_servo[0].throttle=0
finger2=kit.continuous_servo[1].throttle=0
finger3=kit.continuous_servo[2].throttle=0
finger4=kit.continuous_servo[3].throttle=0
finger5=kit.continuous_servo[4].throttle=0
#wrist servos
wristRight=kit.continuous_servo[5].throttle=0
wristLeft=kit.continuous_servo[6].throttle=0
wristHorizontal=kit.continuous_servo[7].throttle=0
#elbow servo
elbow=kit.continuous_servo[8].throttle=0

Sstop=0
Bstop=0.1
#movement pins
wristRWP=MCP3008(channel=1)
wristLWP=MCP3008(channel=2)
wristHP=MCP3008(channel=3)
fingerOP=MCP3008(channel=4)
elbowP=MCP3008(channel=5)

wristRW=0
wristLW=0
wristH=0
fingerO=0
elbow=0
time.sleep(1)
while True:
    if wristRWP.value > 0.5: wristRW=1
    elif wristRWP.value < 0.5: wristRW=-1
    else: wristRW=0
    if wristLWP.value > 0.5: wristLW=1
    elif wristLWP.value < 0.5: wristLW=-1
    else: wristLW=0
    if wristHP.value > 0.5: wristH=1
    elif wristHP.value < 0.5: wristH=-1
    else: wristH=0
    if fingerOP.value > 0.5: fingerO=1
    elif fingerOP.value < 0.5: fingerO=-1
    else: fingerO=0
    if elbowP.value > 0.5: elbow=1
    elif elbowP.value < 0.5: elbow=-1
    else: elbow=0

    finger1.throttle=fingerO
    finger2.throttle=fingerO
    finger3.throttle=fingerO
    finger4.throttle=fingerO
    finger5.throttle=fingerO

    wristRight.throttle=wristRW
    wristLeft.throttle=wristLW
    wristHorizontal.throttle=wristH
    
    elbow.throttle=elbow