import time
import mcp4725_driver as mc
import signal_generator_triangle as sgt
amplitude=3.2
signal_frequency=15
sampling_frequency=1000
try:
    i2c=mc.MCP4725(5.1, 0x61)
    start_time=time.time()
    while True:
        current_time=time.time()-start_time
        signal=sgt.get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage=signal*amplitude
        i2c.set_voltage(voltage)
        sgt.wait_for_sampling_period(sampling_frequency)
except ValueError:
    print("error")        