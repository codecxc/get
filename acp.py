import RPi.GPIO as GPIO
import time

class R2R_DAC:
    def __init__(self,gpio_bits,dynamic_range,comporator_pin):
        self.gpio_bits=gpio_bits
        self.dynamic_range=dynamic_range
        self.comporator_pin=comporator_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits,GPIO.OUT,initial=0)
        GPIO.setup(self.comporator_pin,GPIO.IN)
    def deinit(self):
        GPIO.output(self.gpio_bits,0)
        GPIO.cleanup()
    def set_number(self,voltage):
        value=int(voltage/self.dynamic_range*255)
        current=0
        while current!=number:
            if current<number: current+=1
            else: current-=1
        binary=[int(element) for element in bin(value)[2:].zfill(8)]
        GPIO.output(self.gpio_bits,binary)
        print(f"Число на вход ЦАП: {number}, биты: {binary}")
    def read(self):
        left=0
        # self.set_number(2)
        time.sleep(2)
        h=255
        voltage=0
        while left<=h:
            m=(h+left)//2
            test=m*self.dynamic_range/255
            self.set_number(test)
    
            time.sleep(0.001)
        GPIO.output(self.gpio_bits,0)    
        if GPIO.input(self.comporator_pin):
            target_value=m
            left=m+1
            GPIO.output(self.gpio_bits,1)

        else: h-=1
        return target_value*self.dynamic_range/255
    def generate(self,speed=0.01):
        try:
            while True:
                target_voltage=self.read()
                voltage=0.0
                while voltage<target_voltage:
                    self.set_number(voltage)
                    voltage+=speed
                    time.sleep(0.01)
                self.set_number(target_voltage)
                time.sleep(0.1)
                voltage=target_voltage
                while voltage>0:
                    self.set_number(voltage)
                    voltage-=speed
                    time.sleep(0.01)