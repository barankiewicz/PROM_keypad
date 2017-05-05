import time
import sys
import random
import os
import curses
import RPi.GPIO as GPIO
from data_bus import key2pi, pi2key
from CFG import *
from keypadRead import keypadRead

#CONSTANTS



def number():
    time.sleep(0.1)
    return random.randint(0, 9)

def console_clear():
    #os.system('cls')    #for windows
    os.system('clear')  #for linux
    return



def timeout():
    console_clear()
    for i in range(TIMEOUT + 1):
        sys.stdout.write(" TIMEOUT........%s\r" % (TIMEOUT - i))
        time.sleep(1)
        sys.stdout.flush()

def flash_green():
    pi2key()
    GPIO.output(DATA0, 1)  #MSB
    GPIO.output(DATA1, 0)
    GPIO.output(DATA2, 0) #LSB
    time.sleep(3)
    return

def flash_red():
    pi2key()
    GPIO.output(DATA0, 1)  #MSB
    GPIO.output(DATA1, 0)
    GPIO.output(DATA2, 1) #LSB
    time.sleep(1)
    GPIO.cleanup()
    return

def buzzer():
    return

def ReadFromFile(filename):
    try:
        f = open("password.txt", 'r')
        password = f.readline()
        f.close()
    except IOError:
        password = '1234'
    return password


def passwordRead(password):
    password_input = ''
    sys.stdout.flush()
    console_clear()
    sys.stdout.write("Enter password:\n")
    for i in range(len(password)-1):
        letter = str(keypadRead())
        password_input += letter

        sys.stdout.write("\r%s%s" % ('*'*(len(password_input)-1), password_input[-1]))
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r%s" % ('*'*len(password_input)))
        sys.stdout.flush()
        if (password[i] != letter):
            sys.stdout.write("\nACCESS DENIED \n")
            flash_red()
            return False

    sys.stdout.write("\nACCESS GRANTED \n")
    flash_green()
    return True


try:
    while(True):
        if (MAXIMUM_TRIES == 0):
            passwordRead(ReadFromFile("password.txt"))
        else:
            tries = 0
            while(tries < MAXIMUM_TRIES):
                result = passwordRead(ReadFromFile("password.txt"))
                if not result:
                    sys.stdout.flush()
                    sys.stdout.write("\nWRONG \n")
                    sys.stdout.flush()
                    tries += 1

            timeout()

except KeyboardInterrupt:
    console_clear()
    print("KEYBOARD INTERRUPT")
