import time
import sys
import random
import os

#CONSTANTS

MAXIMUM_TRIES = 2
TIMEOUT = 5


def number():
    time.sleep(0.1)
    return random.randint(0, 9)

def console_clear():
    os.system('cls')    #for windows
    os.system('clear')  #for linux

def timeout(seconds):
    console_clear()
    for i in range(seconds+1):
        sys.stdout.write("\r TIMEOUT........%s" % (seconds - i))
        time.sleep(1)

def flash_red():
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
            if (password[i] != letter):
                tries += 1
                flash_red()
                time.sleep(1)
                break
            time.sleep(1)
            sys.stdout.write("\r%s" % ('*'*len(password_input)))
            sys.stdout.flush()

    timeout(TIMEOUT)


try:
    while(True):
        passwordRead(passwordReadFromFile("password.txt"))
except KeyboardInterrupt:
    print("lol")
