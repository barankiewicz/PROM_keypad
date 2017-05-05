import RPi.GPIO as GPIO
import time
import CFG

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
controls = (17,15) #list of control wires
inputs = (9,10,11)
GPIO.setup(controls, GPIO.OUT)
GPIO.output(17, True) #disable LOAD
GPIO.output(15, False) #disable LOAD

GPIO.setup(inputs, GPIO.OUT)

GPIO.output(inputs, False)

time.sleep(5)

GPIO.output(15, True) #disable LOAD
GPIO.output(17, False) #disable LOAD
print("Begin input")

GPIO.setup(inputs, GPIO.IN)

while(True):
    temp = (GPIO.input(9), GPIO.input(10), GPIO.input(11))
    print("Input: " + str(temp))
    time.sleep(5)
