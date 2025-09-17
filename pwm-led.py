import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
photo=6
led=26
GPIO.setup(photo,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
pwm=GPIO.PWM(led,40)
duty=0.0
pwm.start(duty)
a=True
while a:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.1)
    duty+=1
    if duty>100:
        duty=0.0
