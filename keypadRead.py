import RPi.GPIO as GPIO
import time
from data_bus import key2pi, pi2key
from CFG import *

###### INITIAL SETUP ############################

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROLS, GPIO.OUT)

#################################################

def test():
    pi2key()
    GPIO.output(DATA0, 0)  #MSB
    GPIO.output(DATA1, 0)
    GPIO.output(DATA2, 1) #LSB
    time.sleep(60)

def keypadRead():
    f = open('times.txt', 'a')
    while(True):
        for i in range(4): #loop through the rows
            pi2key()
            GPIO.output(DATA0, MAP[i][0])  #MSB
            GPIO.output(DATA1, MAP[i][1])
            GPIO.output(DATA2, MAP[i][2]) #LSB
            key2pi()

            start = time.time()
            column_input = (GPIO.input(DATA2), GPIO.input(DATA1), GPIO.input(DATA0))
            for j in range(3): #loop through the columns
                if (column_input == MAP_ONEHOT[j]):
                    time.sleep(0.01) #debounce???
                    if(column_input == MAP_ONEHOT[j]):
                        f.write('key pressed: ' + str(MATRIX[i][j]) + ', time: ' + str(time.time() - start) + '\n')
                        return MATRIX[i][j]


def ledcount(dur):
    GPIO.setmode(GPIO.BCM)
    leds = (5, 6, 12, 13, 16, 19, 20, 26)
    GPIO.setup(leds, GPIO.OUT)
    try:
        GPIO.output(leds, False)
        single_time = dur/8
        for i in range(8):
            GPIO.output(leds[i],True)
            time.sleep(single_time)
        GPIO.output(leds, False)
    except KeyboardInterrupt:
        GPIO.output(leds, False)


# ledcount(2.0)
# ledcount(2.0)
# ledcount(2.0)
# ledcount(2.0)
