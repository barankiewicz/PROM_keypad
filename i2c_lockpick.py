import RPi.GPIO as GPIO
import smbus, time

def idle(dur):
    start = time.time()
    while float(time.time() - start) < dur:
        bus.write_byte(0x38, 0b11111000)

def column(column, dur):
    if column == 0:
        column0(dur)
    elif column == 1:
        column1(dur)
    elif column == 2:
        column2(dur)

def column0(dur):
    start = time.time()
    while float(time.time() - start) < dur:
        bus.write_byte(0x38, 0b11111100)

def column1(dur):
    start = time.time()
    while float(time.time() - start) < dur:
        bus.write_byte(0x38, 0b11111010)

def column2(dur):
    start = time.time()
    while float(time.time() - start) < dur:
        bus.write_byte(0x38, 0b11111001)

def row_read():
    #a map between the row no and corresponding data bus bits
    MAP = {
    0: '000',
    1: '001',
    2: '010',
    3: '011'
    }

    value = bin(bus.read_byte(0x38))[2:5] #take the 3 most significant bits

    for i in range(len(MAP.keys())):
        if map[i] == value:
            return i

    return False

def check_green_led():
    value = bin(bus.read_byte(0x38))[2:][4] #take the 5th bit that corresponds with the green LED
    if value == '0':
        return False
    else:
        return True

def check_red_led():
    value = bin(bus.read_byte(0x38))[2:][3] #take the 6th bit that corresponds with the red LED
    if value == '0':
        return False
    else:
        return True

def drive(char):
    MATRIX = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
    ]
    if char not in MATRIX:
        return

    for i in range(4):
        if char in MATRIX[i]:
            for j in range(3):
                if char == MATRIX[i][j]:
                    column(j, 0.1)

def lockpick():
    MATRIX = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
    ]
    password = ''

    for i in range(4):
        for j in range(3):
            drive(MATRIX[i][j])

bus = smbus.SMBus(1)

while True:
    bus.write_byte( 0x38, 241 )
    time.sleep(1)
    check_green_led()
