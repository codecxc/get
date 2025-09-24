import RPi.GPIO as GPIO
import time     

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
leds=[16,12,25,17,27,23,22,24]
GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds,0)
buttons=[9,10]
GPIO.setup(buttons,GPIO.IN)
num=0
sleep_time=0.2
double_pres=0.5
def check():
    if GPIO.input(buttons[0]):
        time.sleep(0.1)
        if GPIO.input(buttons[1]):
            return True
    elif GPIO.input(buttons[1]):
        time.sleep(0.1)
        if GPIO.input(buttons[0]):
            return True
while True:
    if check():
        num=255
    elif GPIO.input(buttons[0]):
        if(num==255): continue
        else:
            num+=1
            print(num,dec2bin(num))
            time.sleep(sleep_time)
    elif GPIO.input(buttons[1]):
        if(num==0): continue
        else:
            if(num==255): num=0
            else:
                num-=1
                print(num,dec2bin(num))
                time.sleep(sleep_time)
    GPIO.output(leds,dec2bin(num))