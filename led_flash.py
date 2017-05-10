import RPi.GPIO as GPIO
from CFG import *
import time
from data_bus import *

def flash_green():
    '''
    This function drives the data to the GPIO lines that correspond with a green LED.
    It lights up the green LED for 3 seconds.
    '''
    pi_to_key()
    GPIO.output(DATA0, 1)  #MSB
    GPIO.output(DATA1, 0)
    GPIO.output(DATA2, 0) #LSB
    time.sleep(3)
    return

def flash_red():
    '''
    This function drives the data to the GPIO lines that correspond with a red LED.
    It lights up the green LED for 3 seconds.
    '''
    pi_to_key()
    GPIO.output(DATA0, 1)  #MSB
    GPIO.output(DATA1, 0)
    GPIO.output(DATA2, 1) #LSB
    time.sleep(1)
    GPIO.cleanup()
    return
