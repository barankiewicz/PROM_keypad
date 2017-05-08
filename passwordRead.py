import time
import sys
import random
import os
import RPi.GPIO as GPIO
import csv
from data_bus import key2pi, pi2key
from CFG import *
from keypadRead import keypadRead

def logtime_start():
    with open('log.csv', 'a') as csvfile:
        log = csv.writer(csvfile, delimiter = ' ')
        log.writerow(['Started the lock: '] +
        [time.gmtime(time.time()).tm_year] +
        [time.gmtime(time.time()).tm_mon] +
        [time.gmtime(time.time()).tm_mday] +
        [time.gmtime(time.time()).tm_hour] +
        [time.gmtime(time.time()).tm_min] +
        [time.gmtime(time.time()).tm_sec])

def logtime_end():
    with open('log.csv', 'a') as csvfile:
        log = csv.writer(csvfile, delimiter = ' ')
        log.writerow(['Ended the lock: '] +
        [time.gmtime(time.time()).tm_year] +
        [time.gmtime(time.time()).tm_mon] +
        [time.gmtime(time.time()).tm_mday] +
        [time.gmtime(time.time()).tm_hour] +
        [time.gmtime(time.time()).tm_min] +
        [time.gmtime(time.time()).tm_sec])

def logtime(result):
    with open('log.csv', 'a') as csvfile:
        log = csv.writer(csvfile, delimiter = ' ')
        log.writerow(['Entered combination'] +
        [time.gmtime(time.time()).tm_year] +
        [time.gmtime(time.time()).tm_mon] +
        [time.gmtime(time.time()).tm_mday] +
        [time.gmtime(time.time()).tm_hour] +
        [time.gmtime(time.time()).tm_min] +
        [time.gmtime(time.time()).tm_sec] +
        [result])

def console_clear():
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

def time_lockout():
    if START_TIME == END_TIME:
        return True
    else:
        current_hour = time.localtime(time.time()).tm_hour

        if current_hour > START_TIME and current_hour < END_TIME:
            return True
        else:
            return False

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
        if i == 0:
            letter = str(keypadRead())
        else:
            letter = str(keypadRead(INTER_DIGIT))

        password_input += letter

        sys.stdout.write("\r%s%s" % ('*'*(len(password_input)-1), password_input[-1]))
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r%s" % ('*'*len(password_input)))
        sys.stdout.flush()
        if (password[i] != letter):
            logtime(False)
            sys.stdout.write("\nACCESS DENIED\n")
            flash_red()
            return False

    sys.stdout.write("\nACCESS GRANTED\n")
    logtime(True)
    flash_green()
    return True

def main():
    logtime_start()
    try:
        while True:
            if time_lockout():
                if (MAXIMUM_TRIES == 0):
                    passwordRead(ReadFromFile("password.txt"))
                else:
                    tries = 0
                    while(tries < MAXIMUM_TRIES):
                        result = passwordRead(ReadFromFile("password.txt"))
                        if not result:
                            tries += 1

                    timeout()
            else:
                sys.stdout.flush()
                sys.stdout.write("\nThe lock is closed at this time of the day\n")
                sys.stdout.flush()
                time.sleep(5)


    except KeyboardInterrupt:
        console_clear()
        logtime_end()
        print("KEYBOARD INTERRUPT")

main()
