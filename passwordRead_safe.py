import RPi.GPIO as GPIO
import time, sys, os
from data_bus import *
from CFG import *
from keypadRead import keypadRead
from logfile import *
from timeLockout import time_lockout

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

def ReadFromFile(filename):
    try:
        f = open("password.txt", 'r')
        password = f.readline()
        f.close()
    except IOError:
        password = '1234'
    return password

def safe_passwordRead(password):
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


    if (password_input != password):
        logtime(False)
        sys.stdout.write("\nACCESS DENIED\n")
        flash_red()
        return False
    else:
        sys.stdout.write("\nACCESS GRANTED\n")
        logtime(True)
        flash_green()
        return True

def safe_main():
    logtime_start()
    try:
        while True:
            if time_lockout():
                if (MAXIMUM_TRIES == 0):
                    safe_passwordRead(ReadFromFile("password.txt"))
                else:
                    tries = 0
                    while(tries < MAXIMUM_TRIES):
                        result = safe_passwordRead(ReadFromFile("password.txt"))
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



safe_main()
