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

def keypadRead():
    #a matrix representing the keypad
    matrix = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'B'],
    [7, 8, 9, 'C'],
    ['*', 0, '#', 'D']
    ]

    #a dictionary that maps rows/columns numbers to wire arrangement
    map = {
    0: (False,False,False), #000
    1: (False,False,True),  #001
    2: (False,True,False),  #010
    3: (False,True,True)    #011
    }

    map_onehot = {
    0: (False, True, True),
    1: (True, False, True),
    2: (True, True, False)
    }

    try:
        while(True):
            print("chuj")
            for i in range(4): #loop through the rows
                pi2key()
                GPIO.output(9, map[i][0])  #MSB
                GPIO.output(10, map[i][1])
                GPIO.output(11, map[i][2]) #LSB
                time.sleep(0.01)
                key2pi()
                column_input = (GPIO.input(11), GPIO.input(10), GPIO.input(9))
                for j in range(3): #loop through the columns
                    if(column_input == map_onehot[j]):
                        time.sleep(0.01) #debounce???
                        if(column_input == map_onehot[j]):
                            return matrix[i][j]
    except KeyboardInterrupt:
        GPIO.cleanup()
        return

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
#
#
# ledcount(0.05)
# ledcount(0.05)
# ledcount(0.05)
# ledcount(0.05)
# ledcount(0.05)
# ledcount(0.05)
# ledcount(0.05)
# ledcount(0.05)
# ledcount(0.05)


keypadRead()
keypadRead()
keypadRead()

# try:
#     f = open("password.txt", 'r')
#     password = f.readline()
#     f.close()
# except IOError:
#     password = '1234'
#
# print(password)
# for i in range(len(password)-1):
#     letter = str(keypadRead())
#     if (password[i] != letter):
#         print("Wrong password")
#         print("should be", password[i])
#         time.sleep(1)
