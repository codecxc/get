import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self,gpio_pin,pwm_frequency,dynamic_range):
        self.gpio_pin=gpio_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin,GPIO.OUT)
        self.dynamic_range=dynamic_range
        self.pwm_frequency=pwm_frequency
        self.pwm=GPIO.PWM(self.gpio_pin,self.pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup()
    def set_voltage(self,voltage):
        if not(0.0<=voltage<=self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.0-{self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            voltage=0.0
        duty=(voltage/self.dynamic_range)*100
        self.pwm.ChangeDutyCycle(duty)
 #       print(f"Коэффицент заполнения {duty}")
if __name__=="__main__":
    try:
        dac=PWM_DAC(12,500,3.177)
        while True:
            try:
                voltage=float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()