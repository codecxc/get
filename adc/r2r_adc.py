import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self,dynamic_range,compare_time=0.005,verbose=False):
        self.dynamic_range=dynamic_range
        self.verbose=verbose
        self.compare_time=compare_time

        self.bits_gpio=[26,20,19,16,13,12,25,11]
        self.comp_gpio=21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio,GPIO.OUT,initial=0)
        GPIO.setup(self.comp_gpio,GPIO.IN)
    def deinit(self):
        for i in self.bits_gpio:
            GPIO.output(i,0)
        GPIO.cleanup()
    def number_to_dac(self,number):
        binary=[int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio,binary)
    def sequential_counting_adc(self):
        for i in range(256):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            comporator=GPIO.input(self.comp_gpio)

            if(comporator==1):
                print(f'Число {i}')
                return i
        print(f'Максимальное число {255}')
        return 255
    def get_sc_voltage(self):
        voltage=self.sequential_counting_adc()*self.dynamic_range/255
        print(f'Напряжение {voltage}') #2.7=219*d/255
        return voltage
# if __name__=="__main__":
#     try:
#         dac=R2R_ADC(3.21)
#         while True:
#             try:
#                 dac.get_sc_voltage()
#             except ValueError:
#                 print("")
#     finally:
#         dac.deinit()