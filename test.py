from global_variables import *
from console_clear import *
#from _lock import lock
import sys

'''
TODO:
1) Make the password editable from the menu
2) Change the input from dico to lists to maintain the order of the CSV
'''

def print_line(i, dico):
    min_choice = 0
    max_choice = len(dico.keys()) - 1
    result = ''
    result += str(i) + ". "
    result += str(dico[i][0])
    result += ', * - up, # - down, 5 - edit, 0 - return'
    print(result)
    # console_clear()
    # sys.stdout.flush()
    # sys.stdout.write(result)
    # sys.stdout.flush()
    choice = input()

    if str(choice) == '*':
        if (i + 1) > max_choice:
            return print_line(i, dico)
        else:
            i += 1
            return print_line(i, dico)
    elif str(choice) == '#':
        if (i - 1) < min_choice:
            return print_line(i, dico)
        else:
            i -= 1
            return print_line(i, dico)
    elif str(choice) == '5':
        return edit_line(dico[i][0])
        print('')
    elif str(choice) == '0':
        print('')
        #lock()
    else:
        return print_line(i, dico)

def edit_line(var):
    # sys.stdout.flush()
    dico = read()
    result = ''
    result += str(var) + ', current value: '
    result += str(dico[var])
    result += ', 5 - edit, 0 - return'
    print(result)

    # console_clear()
    # sys.stdout.flush()
    # sys.stdout.write(result)
    # sys.stdout.flush()

    choice = input()
    if choice == '5':
        return edit_value(var, dico)
    elif choice == '0':
        return print_line(0, read_menu())

def edit_value(var, dico):
    result = ''
    new = ''
    result += 'Enter new value (* - return, # - enter): '


    while(True):
        # sys.stdout.flush()
        # console_clear()
        # sys.stdout.flush()
        # sys.stdout.write(result)
        # sys.stdout.flush()
        print(new)
        print(result)
        choice = input()
        if choice == '*':
            return print_line(0, read_menu())
        elif choice == '#' and len(new) == 0:
            return edit_value(var, dico)
        elif choice == '#' and len(new) != 0:
            dico[var] = int(new)
            write(dico)
            return print_line(0, read_menu())
        else:
            new += choice
            result += choice

print_line(0, read_menu())
