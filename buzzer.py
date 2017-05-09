import RPi.GPIO as GPIO
import time
from data_bus import key2pi, pi2key
from CFG import *

def buzzer(dur = 0.2):
    '''
    Buzzes the buzzer at 1kHz for specified amount of seconds.
    By default, it buzzes for 0.2 seconds.
    '''
    pi2key()
    start = time.time()
    while float(time.time() - start) < dur:
        GPIO.output(DATA0, 1)  #MSB
        GPIO.output(DATA1, 1)
        GPIO.output(DATA2, 0) #LSB
        time.sleep(0.001)
        GPIO.output(DATA0, 0)  #MSB
        GPIO.output(DATA1, 0)
        GPIO.output(DATA2, 0) #LSB
        time.sleep(0.001)
    return
