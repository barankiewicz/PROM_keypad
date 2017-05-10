import RPi.GPIO as GPIO
import time
from CFG import *

def pi_to_key():
    '''
    This function sets the bi-directional data bus in the Pi-to-keypad mode
    '''
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CONTROLS, GPIO.OUT)
    GPIO.output(LOAD, True) #disable LOAD
    GPIO.output(OUTPUT_ENABLE, False) #enable OUTPUT-ENABLE
    time.sleep(0.01)
    GPIO.setup(DATABUS, GPIO.OUT)

def key_to_pi():
    '''
    This function sets the bi-directional data bus in the keypad-to-Pi mode
    '''
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CONTROLS, GPIO.OUT)
    GPIO.output(LOAD, False) #disable LOAD
    GPIO.output(OUTPUT_ENABLE, True) #enable OUTPUT-ENABLE
    time.sleep(0.01)
    GPIO.setup(DATABUS, GPIO.IN)
