import RPi.GPIO as GPIO
import time
from CFG import *

def pi2key():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CONTROLS, GPIO.OUT)
    GPIO.output(LOAD, True) #disable LOAD
    GPIO.output(OUTPUT_ENABLE, False) #enable OUTPUT-ENABLE
    time.sleep(0.01)
    GPIO.setup(DATABUS, GPIO.OUT)

def key2pi():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CONTROLS, GPIO.OUT)
    GPIO.output(LOAD, False) #disable LOAD
    GPIO.output(OUTPUT_ENABLE, True) #enable OUTPUT-ENABLE
    time.sleep(0.01)
    #GPIO.setup(inputs, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(DATABUS, GPIO.IN)
