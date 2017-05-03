import time
import sys
import random
import os
import curses
import RPi.GPIO as GPIO
from data_bus import key2pi, pi2key
import CFG

#CONSTANTS



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

def flash_green():
    pi2key()
    GPIO.output(9, 1)  #MSB
    GPIO.output(10, 0)
    GPIO.output(11, 0) #LSB
    time.sleep(3)
    return

def flash_red():
    pi2key()
    GPIO.output(9, 1)  #MSB
    GPIO.output(10, 0)
    GPIO.output(11, 1) #LSB
    time.sleep(1)
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
    sys.stdout.write("Enter password:")
    for i in range(len(password)-1):
        letter = str(keypadRead())
        password_input += letter

        sys.stdout.write("\r%s%s" % ('*'*(len(password_input)-1), password_input[-1]))
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\r%s" % ('*'*len(password_input)))
        sys.stdout.flush()
        if (password[i] != letter):
            #flash_red()
            return False
    return True


try:
    while(True):
        passwordRead(passwordReadFromFile("password.txt"))
        #timeout(TIMEOUT)
except KeyboardInterrupt:
    print("lol")
