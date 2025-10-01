import RPi.GPIO as GPIO

leds=[16,20,21,25,26,17,27,22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)
dynamic_range=3.177
def voltage_to_number(voltage):
    if not(0.0<=voltage<=dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.0-{dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage/dynamic_range*255)
def number_to_dac(number):
    binary=[int(element) for element in bin(number)[2:].zfill(8)]
    print(f"Число на вход ЦАП: {number}, биты: {binary}")
    GPIO.output(leds,binary)
    

try:
    while True:
        try:
            voltage=float(input("Введите напряжение в вольтах: "))
            number=voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
finally:
    GPIO.output(leds,0)
    GPIO.cleanup()

