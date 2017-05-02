import time
import sys
import random
import os
import curses
from data_bus import key2pi, pi2key

#CONSTANTS

MAXIMUM_TRIES = 2
TIMEOUT = 5


def number():
    time.sleep(0.1)
    return random.randint(0, 9)

def console_clear():
    #os.system('cls')    #for windows
    os.system('clear')  #for linux
    return



def timeout(seconds):
    console_clear()
    for i in range(seconds+1):
        sys.stdout.write(" TIMEOUT........%s\r" % (seconds - i))
        time.sleep(1)
        sys.stdout.flush()

def flash_green(time):
    pi2key()
    GPIO.output(9, True)  #MSB
    GPIO.output(10, False)
    GPIO.output(11, False) #LSB
    time.sleep(time)
    return

def flash_red(time):
    pi2key()
    GPIO.output(9, True)  #MSB
    GPIO.output(10, False)
    GPIO.output(11, True) #LSB
    time.sleep(time)
    return

def buzzer():
    return

def passwordReadFromFile (filename):
    try:
        f = open("password.txt", 'r')
        password = f.readline()
        f.close()
    except IOError:
        password = '1234'
    return password


def passwordRead(password):
    tries = 0

    while (tries <= MAXIMUM_TRIES-1):
        password_input = ''
        sys.stdout.flush()
        console_clear()
        for i in range(len(password)-1):
            letter = str(number())
            password_input += letter

            sys.stdout.write("\r%s%s" % ('*'*(len(password_input)-1), password_input[-1]))
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write("\r%s" % ('*'*len(password_input)))
            sys.stdout.flush()
            if (password[i] != letter):
                tries += 1
                flash_red(1)
                break



    timeout(TIMEOUT)


try:
    while(True):
        passwordRead(passwordReadFromFile("password.txt"))
        #timeout(TIMEOUT)
except KeyboardInterrupt:
    print("lol")
