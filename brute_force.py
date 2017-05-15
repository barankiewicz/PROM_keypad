from i2c_lockpick import *

def brute_force():
    '''
    This function implements the brute force attack technique.
    It reads the order of the passwords it should check from the file 'brute_force.txt'.
    The file was created with optimization of cracking times in mind.
    The first 20 lines are the 20 most common PINs according to the study held by:
    http://datagenetics.com/blog/september32012/index.html
    For the full discussion on how I improved the cracking times, please refer to my
    individual log I submitted with the code.
    '''

    f = open('brute_force.txt', 'r')

    for row in f:
        password = row
        password = password.strip('\n')

        for letter in password:
            idle(0.5)
            drive_char(letter)
            idle(0.5)

        time.sleep(0.2)
        led = check_red()
        if led == False:
            continue
        else:
            print(row)
            return row
