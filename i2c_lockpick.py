
import smbus, time

def check_leds():
    '''
    This function checks the status of the green and red LEDs in the lock system
    and returns a tuple of their boolean values (RED, GREEN)
    '''
    value = str(format(bus.read_byte(0x38), '#010b'))[2:]
    result = [value[3] == '1', value[4] == '1']
    bus.write_byte(0x38, 0b11111000)
    return tuple(result)

def check_red():
    '''
    This function checks the status of the red LED in the lock system
    and returns it as a boolean
    '''
    value = str(format(bus.read_byte(0x38), '#010b'))[2:]
    bus.write_byte(0x38, 0b11111000)
    return value[3] == '1'

def check_buzz():
    '''
    This function checks the status of the buzzer in the lock system
    and returns it as a boolean
    '''
    start = time.time()
    while float(time.time() - start) < 0.2:
        value = str(format(bus.read_byte(0x38), '#010b'))[2:]
        bus.write_byte(0x38, 0b11111000)
        if value[4] != '1':
            return value[4] != '1'

def column(col):
    '''
    This function drives a 0 onto a row that is passed as an argument
    '''
    bus = smbus.SMBus(1)
    if col == 0:
        bus.write_byte(0x38, 0b11111001)
    elif col == 1:
        bus.write_byte(0x38, 0b11111010)
    elif col == 2:
        bus.write_byte(0x38, 0b11111100)
    elif col == False:
        bus.write_byte(0x38, 0b11111000)
    return

def row_read():
    '''
    This function reads which row the 0 is driven onto by the lock system and returns its number [0..3]
    '''
    bus = smbus.SMBus(1)
    #a map between the row no and corresponding data bus bits
    MAP = {
    '110': 0,
    '010': 1,
    '100': 2,
    '000': 3,
    }
    bus.write_byte(0x38, 0b11111000)
    value = str(format(bus.read_byte(0x38), '#010b'))[2:5] #take the 3 most significant bits
    #value = str(format(bus.read_byte(0x38), '#010b')) #take the 3 most significant bits
    #print(value)
    if value in MAP.keys():
        return MAP[value]
    else:
        return False    

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
    bus.write_byte(0x38, 0b11111000)
    # while True:
    #     if row_read() == row:
    #         while row_read() == row:
    #             column(col)
    #         bus.write_byte(0x38, 0b11111000)
    #         return MATRIX[row][col]

    while check_buzz():
        if row_read() == row:
            while row_read() == row:
                column(col)
    bus.write_byte(0x38, 0b11111000)
    return MATRIX[row][col]




    bus.write_byte(0x38, 0b11111000)
    return MATRIX[row][col]



def drive_char(char):
    '''
    This function drives the symbol onto the lock system.
    '''
    MATRIX = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
    ]

    #first, find out which row and column needs to be driven to drive this char
    col = 0
    row = 0
    for i in range(4):
        if char in MATRIX[i]:
            row = i
            for j in range(3):
                if char == MATRIX[i][j]:
                    col = j

    return drive(row, col)

    #==========================================
    #MATRIX_DECODE = {
    #'1': (0, 0), '2': (0, 1), '3': (0, 2),
    #'4': (1, 0), '5': (1, 1), '6': (1, 2),
    #'7': (2, 0), '8': (2, 1), '9': (2, 2),
    #'*': (3, 0), '0': (3, 1), '#': (3, 2)    
    #}
    #rowCol = MATRIX_DECODE[char]
    #return drive(rowCol[0], rowCol[1])
    #===========================================

def lockpick():
    '''
    This is the main lockpicking function. It returns the password when it detects
    that the green LED has lit up.
    '''
    f = open("cracked_password.txt", 'w')
    bus = smbus.SMBus(1)

    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '#']
    password = ''
    wrong = ''

    while len(password) < 4:
        for char in chars:
            for i in range(len(password)):
                time.sleep(0.5)
                drive_char(password[i])
                time.sleep(0.5)

            drive_char(char)
            time.sleep(0.5)

            led = check_red()
            if led == False:
                wrong = char
                idle(1)
            else:
                password += char
                drive_char(wrong)
                break

    return password

def idle(dur):
    '''
    This function idles for the specific duration - it doesn't drive any
    data onto any of the rows
    '''
    IDLE = 0xF8

    start = time.time()
    while float(time.time() - start) < dur:
        bus.write_byte(I2C_ADDR, IDLE)

bus = smbus.SMBus(1)
I2C_ADDR = 0x38
# while True:
#     print(check_red())

lockpick()
