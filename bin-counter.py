import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
leds=[24,22,23,27,17,25,12,16]

GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds,0)
buttons=[9,10]
GPIO.setup(buttons,GPIO.IN)
sleep_time=0.2
num=0
ch=0
while True:
    if(GPIO.input(buttons[0])):

        if(GPIO.input(buttons[1])):
            for led in leds:
                GPIO.output(led,1)
            ch=1
            time.sleep(0.5)
            continue
    if (num==0):
        if(GPIO.input(buttons[0])):
            if(ch==1): 
                GPIO.output(leds,0)
                ch=0
            GPIO.output(leds[num+1],1)
            GPIO.output(leds[num],0)
            num+=1
            time.sleep(sleep_time)
    elif (num==7):
        if(GPIO.input(buttons[1])):
            if(ch==1): 
                GPIO.output(leds,0)
                ch=0
            GPIO.output(leds[num-1],1)
            GPIO.output(leds[num],0)
            num-=1
            time.sleep(sleep_time)
    else:
        if(GPIO.input(buttons[1])):
            if(ch==1): 
                GPIO.output(leds,0)
                ch=0
            GPIO.output(leds[num-1],1)
            GPIO.output(leds[num],0)
            num-=1
            time.sleep(sleep_time)
        if(GPIO.input(buttons[0])): 
            if(ch==1): 
                GPIO.output(leds,0)
                ch=0
            GPIO.output(leds[num+1],1)
            GPIO.output(leds[num],0)
            num+=1
            time.sleep(sleep_time)