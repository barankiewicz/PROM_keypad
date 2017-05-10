import sys
from data_bus import *
from global_variables import *
from logfile import *
from password_read import *
from time_lockout import *
from timeout import *

def lock():
    '''
    This function ties all the digital lock functionalities into one.
    It acts as an infinite system that can only be turned off with a KeyboardInterrupt.
    It has a number of 'gates' that act as the logic behind in which mode the system should perform.
    (e.g. time lockout, maximum try lockout, safe/vulnerable mode)
    '''
    dico = read()
    logtime_start()
    try:
        while True:
            if time_lockout():
                if dico['SAFE_SYSTEM'] == 0:
                    if dico['MAXIMUM_TRIES'] == 0:
                        password_read(read_from_file())
                    else:
                        tries = 0
                        while tries < dico['MAXIMUM_TRIES']:
                            result = password_read(read_from_file())
                            if not result:
                                tries += 1
                        timeout()

                elif dico['SAFE_SYSTEM'] == 1:
                    if dico['MAXIMUM_TRIES'] == 0:
                        safe_password_read(read_from_file())
                    else:
                        tries = 0
                        while tries < dico['MAXIMUM_TRIES']:
                            result = safe_password_read(read_from_file())
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

lock()
