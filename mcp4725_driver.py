import smbus

class MCP4725:
    def __init__(self,dynamic_range,address):
        self.bus=smbus.SMBus(1)
        self.address=address
        self.wm=0x00
        self.pds=0x00
        self.dynamic_range=dynamic_range
    def deinit(self):
        self.bus.close()

    def set_number(self,number):
        if not isinstance(number,int): 
            print("На вход ЦАП можно подавать только целые числа")
            return
        if not(0<=number<=4095): 
            print("Число выходит за 12бит")
            return
        first_byte=self.wm | self.pds | (number>>8)
        second_byte=number & 0xFF
        self.bus.write_byte_data(self.address, first_byte, second_byte)
        print(f"Число {number}, отправленные по I2C данные: [0x{(self.address<<1):02X},0x{first_byte:02X},0x{second_byte:02X}]\n")
    def set_voltage(self,voltage):
        if not(0.0<voltage<=self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.0-{self.dynamic_range:.2f} В)")
            voltage=0.0                                   
        number=int(voltage/self.dynamic_range *4095)
        self.set_number(number)
if __name__=="__main__":
    try:
        dac=MCP4725(3.177,0x61)
        while True:
            try:
                voltage=float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()