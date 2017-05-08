import RPi.GPIO as GPIO
import time
from data_bus import key2pi, pi2key
from CFG import *

###### INITIAL SETUP ############################

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROLS, GPIO.OUT)

#################################################

def keypadRead(dur = 0):
    '''
    Reads the keypad for the time stated at the INTER_DIGIT time in the config file.
    If no argument is given, it waits for the input until it gets it.
    If an argument is given and time is exceeded, returns 'X'
    '''
    GPIO.setmode(GPIO.BCM)
    leds = (5, 6, 12, 13, 16, 19, 20, 26)
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds, False)

    if dur == 0:
        return poll()
    else:
        single_time = float(dur)/8
        for i in range(8):
            press = poll(single_time)
            if not press:
                GPIO.output(leds[i],True)
            else:
                GPIO.output(leds, False)
                return press

        GPIO.cleanup()
        return 'X'


def poll(dur = 0):
    '''
    Polls for the duration given in seconds.
    If no argument is given, polls until it gets a keypad input
    '''
    if dur == 0:
        while True:
            key = single_poll()
            if not key == False:
                return key
            else:
                continue
    else:
        start = time.time()
        while float(time.time() - start) < dur:
            key = single_poll()
            if not key == False:
                return key
            else:
                continue
        return False

def single_poll():
    '''
    Represents a single poll through the keypad.
    Drives 0 onto rows 0..3 and reads columns input for each of them.
    If one of the columns returns a 0, it returns the value connected to it.
    If it didn't get any 0's on the columns, returns False
    '''
    for i in range(4): #loop through the rows
        pi2key()
        GPIO.output(DATA0, MAP[i][0])  #MSB
        GPIO.output(DATA1, MAP[i][1])
        GPIO.output(DATA2, MAP[i][2]) #LSB
        key2pi()

        column_input = (GPIO.input(DATA2), GPIO.input(DATA1), GPIO.input(DATA0))
        for j in range(3): #loop through the columns
            if (column_input == MAP_ONEHOT[j]):
                time.sleep(0.01) #debounce???
                if(column_input == MAP_ONEHOT[j]):
                    return str(MATRIX[i][j])

    return False
