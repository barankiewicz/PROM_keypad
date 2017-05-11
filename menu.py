from global_variables import *
from console_clear import *
from keypad_read import *
from easter_egg import *
import sys

def print_line(i, dico):
    '''
    This is the main menu function. It reads the CSV config file and outputs it
    in a neat way, then waits for the input for the user.
    '''

    #Initialize the min and max values that the menu can go to (based on the length of the CSV config file)
    min_choice = 0
    max_choice = len(dico.keys()) - 1

    #Create the line in a neat way and write it
    result = ''
    result += str(i + 1) + ". "
    result += str(dico[i][0])
    result += ', # - up, * - down, 5 - edit, 0 - return'

    console_clear()
    sys.stdout.flush()
    sys.stdout.write(result)
    sys.stdout.flush()

    #Wait for the keypad input
    choice = keypad_read()

    if str(choice) == '*': #If the press is *, go 'up' the menu
        if (i + 1) > max_choice: #If it can't go up any more, just print out the same line
            return print_line(i, dico)
        else:
            i += 1
            return print_line(i, dico)
    elif str(choice) == '#': #If the press is #, go 'down' the menu
        if (i - 1) < min_choice: #If it can't go down any more, just print out the same line
            return print_line(i, dico)
        else:
            i -= 1
            return print_line(i, dico)
    elif str(choice) == '5': #If the press is 5, initialize the edit function for the current variable
        return edit_line(dico[i][0])
    elif str(choice) == '0': #If the press is 0, return to the main lock function
        return
    else: #if the press is none of the above, just print out the same line
        return print_line(i, dico)

def edit_line(var):
    '''
    This function displays the current value of the specific config variable
    and acts as a gateway for the function where the user can actually edit the
    variable.
    '''

    if var == 'STAR_WARS': #EASTER EGG!!!
        time.sleep(0.5)
        star_wars()
        return print_line(0, read_menu())


    #Create the line in a neat way and write it
    sys.stdout.flush()
    dico = read()
    result = ''
    result += str(var) + ', current value: '
    result += str(dico[var])
    result += ', 5 - edit, 0 - return'

    console_clear()
    sys.stdout.flush()
    sys.stdout.write(result)
    sys.stdout.flush()

    #Wait for the keypad input
    choice = keypad_read()

    if choice == '5': #If the press is 5, initialize the edit_value function
        return edit_value(var, dico)
    elif choice == '0': #If the press is 0, restart the menu
        return print_line(0, read_menu())
    else: #if the press is none of the above, just print out the same line
        return edit_line(var)

def bool_parser(var, char):
    '''
    Parser for bool values.
    Only allows 0 or 1.
    '''
    new = var + char
    return new in ['0', '1']

def num_parser(var, char):
    '''
    Parser for numerical values.
    Doesn't allow the password to be longer than 4 digits
    '''
    new = var + char
    return  not len(new) > 3

def time_parser(var, char):
    '''
    Parser for time values.
    Only allows 0-23 values (24-hour clock)
    '''
    legal_values = [str(i) for i in range(0,23)]
    new = var + char
    return new in legal_values

def password_parser(var, char):
    '''
    Parser for the passwords.
    Doesn't allow the password to be longer than 4 digits
    '''
    new = var + char
    return not len(new) > 4

def parser(variable, prev, char):
    '''
    This is the main parser function that detects what is the type of the variable
    in question and returns the according parser function
    '''
    if variable in ['SAFE_SYSTEM']:
        return bool_parser(prev, char)
    elif variable in ['START_TIME', 'END_TIME']:
        return time_parser(prev, char)
    elif variable in ['PASSWORD', 'ADMIN_PASSWORD']:
        return password_parser(prev, char)
    elif variable in ['MAXIMUM_TRIES', 'TIMEOUT']:
        return num_parser(prev, char)


def edit_value(var, dico):
    '''
    This function lets the user edit and update the variable in the csv file.
    '''

    result = '' #this var will be printed out at each loop instance
    new = '' #this var will hold the new value
    result += 'Enter new value (* - return, # - enter): '

    while(True):
        #print the line
        sys.stdout.flush()
        console_clear()
        sys.stdout.write(result)
        sys.stdout.flush()

        #Wait for the keypad input
        choice = keypad_read()

        if choice == '*': #if the press is *, restart the menu
            return print_line(0, read_menu())
        elif choice == '#' and len(new) == 0: #if the press is # but no new value has been entered, just print out the same line
            return edit_value(var, dico)
        elif choice == '#' and len(new) != 0: #if the press is # and a new value has been entered, update the csv file and return to the main menu
            dico[var] = int(new)
            write(dico)
            return print_line(0, read_menu())
        else: #Pass the value through the parser
            if parser(var, new, choice):
                print('True')
                new += choice
                result += choice
            else:
                continue
