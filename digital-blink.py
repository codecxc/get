import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led=26
GPIO.setup(led,GPIO.OUT)
state=0
period=2.0
a=True
while a:
    GPIO.output(led,state)
    state=not(state)
    time.sleep(period)