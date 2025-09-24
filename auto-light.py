import RPi.GPIO as GPIO
#import time


GPIO.setmode(GPIO.BCM)
photo=6
led=26
GPIO.setup(photo,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
#state=0
#period=0.2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
a=True
while a:
    res=GPIO.input(photo)
    GPIO.output(led,not(res))