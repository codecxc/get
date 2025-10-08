import time
import pwm_dac as pd
import signal_generator_triangle as sgt
amplitude=3.2
signal_frequency=15
sampling_frequency=1000
try:
    pds=pd.PWM_DAC(12, 1000, 3.3)
    start_time=time.time()
    while True:
        current_time=time.time()-start_time
        signal=sgt.get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage=signal*amplitude
        pds.set_voltage(voltage)
        sgt.wait_for_sampling_period(sampling_frequency)
except ValueError:
    print("error")