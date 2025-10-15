import r2r_dac as r2r
import signal_generator_triangle as sgt
import time

amplitude=5
signal_frequency=15
sampling_frequency=1000
try:
    dac=r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.3)
    start_time=time.time()
    while True:
        current_time=time.time()-start_time
        signal=sgt.get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage=signal*amplitude
        dac.set_voltage(voltage)
        sgt.wait_for_sampling_period(sampling_frequency)
except ValueError:
    print("error")