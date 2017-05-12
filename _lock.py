import sys
from data_bus import *
from global_variables import *
from logfile import *
from password_read import *
from time_lockout import *
from timeout import *
import datetime

def lock():
    '''
    This function ties all the digital lock functionalities into one.
    It acts as an infinite system that can only be turned off with a KeyboardInterrupt.
    It has a number of 'gates' that act as the logic behind in which mode the system should perform.
    (e.g. time lockout, maximum try lockout, safe/vulnerable mode)
    '''

    logtime_start()
    try:
        while True:
            dico = read()
            if time_lockout():
                if dico['SAFE_SYSTEM'] == 0:
                    if dico['MAXIMUM_TRIES'] == 0:
                        dico = read()
                        password_read(read_from_file())
                        dico = read()
                    else:
                        dico = read()
                        tries = 0
                        while tries < dico['MAXIMUM_TRIES']:
                            result = password_read(read_from_file())
                            dico = read()
                            if result == False:
                                tries += 1
                            else:
                                tries = 0
                        timeout()

                elif dico['SAFE_SYSTEM'] == 1:
                    if dico['MAXIMUM_TRIES'] == 0:
                        dico = read()
                        safe_password_read(read_from_file())
                    else:
                        dico = read()
                        tries = 0
                        while tries < dico['MAXIMUM_TRIES']:
                            result = safe_password_read(read_from_file())
                            dico = read()
                            if result == False:
                                tries += 1
                            else:
                                tries = 0
                        timeout()
            else:
                sys.stdout.flush()
                console_clear()
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                sys.stdout.write(st + "\n")
                sys.stdout.write("The lock is closed at this time of the day\n")
                sys.stdout.flush()
                time.sleep(1)


    except KeyboardInterrupt:
        console_clear()
        logtime_end()
        print("KEYBOARD INTERRUPT")

lock()
