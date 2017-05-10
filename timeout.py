import sys, time
from console_clear import console_clear
from global_variables import read

def timeout():
    '''
    This function implements a part of the 'Maximum try lockout' functionality.
    It clears the console and displays the timeout specified in the TIMEOUT
    variable in the config file.
    '''
    dico = read()
    console_clear()
    for i in range(dico['TIMEOUT'] + 1):
        sys.stdout.write(" TIMEOUT........%s\r" % (dico['TIMEOUT'] - i))
        time.sleep(1)
        sys.stdout.flush()
