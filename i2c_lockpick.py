import RPi.GPIO as GPIO
import smbus, time

# 241 - column 2
# 242 - column 1
# 244 - column 0

def idle(dur):
    start = time.time()
    while float(time.time() - start) < dur:
        bus.write_byte(0x38, 0b11111000)

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

bus = smbus.SMBus(1)

# while True:
#
#     tab = [241, 242, 244]
#     bus.write_byte( I2C_ADDR, tab[i%3] )
#     print("DRIVING: " + str(tab[i%3]))
#     time.sleep(5)
#     i += 1
#
#     i2cvalue = bus.read_byte( I2C_ADDR )
#
#     outputString = "INPUT = " + str( i2cvalue )
#
#     print( outputString )
#
#     time.sleep(1)

while True:
    bus.write_byte( 0x38, 241 )
    time.sleep(1)
    check_green_led()
