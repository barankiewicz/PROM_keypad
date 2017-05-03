import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
controls = (14,15) #list of control wires
GPIO.setup(controls, GPIO.OUT)
GPIO.output(14, True) #disable LOAD

time.sleep(120)
