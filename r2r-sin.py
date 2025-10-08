import r2r_dac as r2r
import signal_generator as sg
import time

amplitude=3.2
signal_frequency=10
sampling_frequency=10000
try:
    dac=r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.3)
    start_time=time.time()
    while True:
        current_time=time.time()-start_time
        signal=sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage=signal*amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
except ValueError:
    print("error")