import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
button=13
led=26
GPIO.setup(button,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
state=0
period=0.2
a=True
while a:
    if GPIO.input(button):
        state=not(state)
        GPIO.output(led,state)
        time.sleep(period)