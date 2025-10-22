import r2r_adc
import time
import adc_plot

voltage_values=[]
time_values=[]
duration=5.0

if __name__=="__main__":
    try:
        dac=r2r_adc.R2R_ADC(3.21)
        start_time=time.time()
        while True:
            try:
                if((time.time()-start_time)<duration):
                    voltage_values.append(dac.get_sc_voltage())
                    time_values.append(time.time())
                else: 
                    adc_plot.plot_voltage_vs_time(time_values,voltage_values,3.21)
                    break
        

            except ValueError:
                print("")
    finally:
        dac.deinit()