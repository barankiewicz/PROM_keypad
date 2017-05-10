import sys
from keypad_read import *
from time_lockout import *
from led_display import *
from console_clear import *
from led_flash import *

def read_from_file():
    '''
    This function tries to get the password from the 'password.txt' file.
    If password.txt isn't found, it sets the password to the default value of '1234'
    and returns it.
    '''
    try:
        f = open("password.txt", 'r')
        password = f.readline()
        f.close()
    except IOError:
        password = '1234'
    return password

def password_read(password):
    '''
    This function reads the sequence entered by the user, displays it in the console
    and compares it to the password read from ReadFromFile() function.
    It compares both digit-by-digit, so as soon as the wrong digit is entered,
    it flashed the red LED and returns False. If the whole password was entered
    correctly, it returns True
    '''
    password_input = '' #This variable will hold the sequence entered by the user
    sys.stdout.flush()
    console_clear()
    sys.stdout.write("Enter password:\n")

    for i in range(len(password)-1):
        if i == 0: #If nothing has been entered yet, wait for the input indifinitely
            letter = str(keypad_read())
        else: #If it's the 2nd or nth entered number, wait only for the INTER_DIGIT time
            letter = str(keypad_read(3))

        password_input += letter
        led_display(password_input)

        if (password[i] != letter):
            logtime(False)
            sys.stdout.write("\nACCESS DENIED\n")
            flash_red()
            return False

    sys.stdout.write("\nACCESS GRANTED\n")
    logtime(True)
    flash_green()
    return True

def safe_password_read(password):
    '''
    This function implements the 'Remove side-channel vulnerability' optional
    software functionality. It's the safe version of the basic passwordRead() function.
    It reads the sequence entered by the user, displays it in the console
    and compares it to the password read from ReadFromFile() function.
    It only compares the entered sequence and the password from the file when there
    are 4 digits entered, which makes it safe and not vulnerable for the side-channel
    attacks.
    If the whole password was entered correctly, it returns True.
    '''
    password_input = '' #This variable will hold the sequence entered by the user
    sys.stdout.flush()
    console_clear()
    sys.stdout.write("Enter password:\n")

    for i in range(len(password)-1):
        if i == 0: #If nothing has been entered yet, wait for the input indifinitely
            letter = str(keypad_read())
        else: #If it's the 2nd or nth entered number, wait only for the INTER_DIGIT time
            letter = str(keypad_read(3))

        password_input += letter
        led_display(password_input)

    if password_input == password:
        sys.stdout.write("\nACCESS GRANTED\n")
        logtime(True)
        flash_green()
        return True
    else:
        logtime(False)
        sys.stdout.write("\nACCESS DENIED\n")
        flash_red()
        return False
