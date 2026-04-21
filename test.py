from gpiozero import DigitalInputDevice
import time

pinA6 = DigitalInputDevice(4, pull_up=True)
pinA7 = DigitalInputDevice(14, pull_up=True)

while True:
    print(pinA6.value, pinA7.value)
    time.sleep(0.5)