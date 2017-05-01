import RPi.GPIO as GPIO
import time
from data_bus import key2pi, pi2key

###### INITIAL SETUP ############################
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

inputs = [9, 10, 11] #list of GPIO data wires
controls = (14,15) #list of control wires
GPIO.setup(controls, GPIO.OUT)

#################################################
