import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

inputs = [9, 10, 11] #list of GPIO data wires
controls = (14,15) #list of control wires
GPIO.setup(controls, GPIO.OUT)

def key2pi():
    GPIO.setmode(GPIO.BCM)
    inputs = (9, 10, 11)
    controls = (14,15) #list of control wires
    GPIO.setup(controls, GPIO.OUT)
    GPIO.output(14, False) #disable LOAD
    GPIO.output(15, True) #enable OUTPUT-ENABLE
    time.sleep(0.01)
    GPIO.setup(inputs, GPIO.OUT)

def pi2key():
    GPIO.setmode(GPIO.BCM)
    inputs = (9, 10, 11)
    controls = (14,15) #list of control wires
    GPIO.setup(controls, GPIO.OUT)
    GPIO.output(14, True) #disable LOAD
    GPIO.output(15, False) #enable OUTPUT-ENABLE
    time.sleep(0.01)
    #GPIO.setup(inputs, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(inputs, GPIO.IN)


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
    0: (True, False, False),
    1: (False, True, False),
    2: (False, False, True)
    }

    try:
        while(True):
            for i in range(4): #loop through the rows
                key2pi()
                GPIO.output(9, map[i][0])  #MSB
                GPIO.output(10, map[i][1])
                GPIO.output(11, map[i][2]) #LSB
                time.sleep(0.01)
                pi2key()
                column_input = (GPIO.input(11), GPIO.input(10), GPIO.input(9))
                for j in range(3): #loop through the columns
                    if(column_input == map_onehot[j]):
                        time.sleep(0.01) #debounce???
                        if(column_input == map_onehot[j]):
                            return matrix[i][j]
    except KeyboardInterrupt:
        GPIO.cleanup()
        return

def test():
    GPIO.setmode(GPIO.BCM)
    controls_in = (9, 10, 11)
    controls_out = (14, 15, 8)
    GPIO.setup(controls_in, GPIO.IN)
    GPIO.setup(controls_out, GPIO.OUT)
    GPIO.output(controls_out, True)
    inputs = (GPIO.input(9), GPIO.input(10), GPIO.input(11))
    print(str(inputs))
    return

def ledcount(dur):
    #dur = float(dur)
    GPIO.setmode(GPIO.BCM)
    leds = (5, 6, 12, 13, 16, 19, 20, 26)
    GPIO.setup(leds, GPIO.OUT)
    single_time = dur/8
    for i in range(8):
        GPIO.output(leds[i],True)
        time.sleep(single_time)
    GPIO.output(leds, False)

ledcount(1.5)
# keypadRead()
# keypadRead()
# keypadRead()

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
