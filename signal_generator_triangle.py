#import numpy as np
import time

def get_triangle_wave_amplitude(freq,time):
    period=1/freq
    p=time%period/period
    if p<0.5: return p*2
    else: return 2-p*2#2-p*2 #(np.sin(2*np.pi*freq*time)+1)/2#2-p*2    
#    return (np.abs(2*np.pi*freq*time)+1)/10000
def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)