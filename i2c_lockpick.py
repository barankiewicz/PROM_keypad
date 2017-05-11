
import smbus, time

def check_leds():
    '''
    This function checks the status of the green and red LEDs in the lock system
    and returns a tuple of their boolean values (RED, GREEN)
    '''
    value = bin(bus.read_byte(0x38))[2:]
    result = [value[3] == '1', value[4] == '1']
    return tuple(result)

def column(col):
    '''
    This function drives a 0 onto a row that is passed as an argument
    '''
    bus = smbus.SMBus(1)
    if col == 0:
        bus.write_byte(0x38, 0b11111100)
    elif col == 1:
        bus.write_byte(0x38, 0b11111010)
    elif col == 2:
        bus.write_byte(0x38, 0b11111001)

    time.sleep(0.01)
    return

def row_read():
    '''
    This function reads which row the 0 is driven onto by the lock system and returns its number [0..3]
    '''
    bus = smbus.SMBus(1)
    #a map between the row no and corresponding data bus bits
    MAP = {
    '111': 0,
    '110': 1,
    '101': 2,
    '100': 3,
    '000': False
    }

    value = bin(bus.read_byte(0x38))[2:5] #take the 3 most significant bits
    #value = bin(bus.read_byte(0x38)) #take the 3 most significant bits

    if value in MAP.keys():
        return MAP[value]
    else:
        raise new Exception("dobra dupa")

def drive(row, col):
    '''
    This function drives the symbol corresponding to the row and the col of the
    3x4 keypad MATRIX. (It waits for the correct row to be driven by the lock system
    and then drives a 0 onto the correct column)
    '''
    MATRIX = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
    ]

    bus = smbus.SMBus(1)
    while True:
        if row_read() == row:
            column(col)
            time.sleep(0.01)
            return

def lockpick():
    '''
    This is the main lockpicking function. It returns the password when it detects
    that the green LED has lit up.
    '''
    MATRIX = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
    ]
    f = open("cracked_password.txt", 'w')
    bus = smbus.SMBus(1)
    password = ''

    bus = smbus.SMBus(1)
    while True: #Loop through the driving algorithm until the green LED lights up
        row = 0
        col = 0
        for row in range(4):
            for col in range(3):
                drive(row, col)
                leds = check_leds()

                if leds[0] == True: #If the red LED lights up, check the next digit after waiting for 1s
                    idle(1)
                    continue
                elif leds[0] == False and leds[1] == False: #if no LEDs light up, add the digit to the password and continue
                    password += MATRIX[row][col]
                elif leds[1] == True: #if the green LED lights up, add the digit to the password and return it, the lock is picked!
                    password += MATRIX[row][col]
                    f.write(password)
                    return

def idle(dur):
    '''
    This function idles for the specific duration - it doesn't drive any
    data onto any of the rows
    '''
    IDLE = 0xF8

    start = time.time()
    while float(time.time() - start) < dur:
        time.sleep(0.01)
        bus.write_byte(I2C_ADDR, IDLE)

bus = smbus.SMBus(1)
I2C_ADDR = 0x38

while(True):
    time.sleep(1)
    row_read()
