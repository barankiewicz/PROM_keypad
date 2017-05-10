import time
from global_variables import read

def time_lockout():
    '''
    This function implements the 'Time lockout' optional software functionality.
    It takes the current UTC time from the time library and checks the config file
    to see if the current time is inbetween the hours set in the config file.
    If it is, returns True.
    If it isn't, returns False.
    If both starting and working hours read from the cfg are the same,
    it means the 'Time lockout' functionality is turned off. If the function detects such
    a case, it returns True.
    '''
    dico = read()

    if dico['START_TIME'] == dico['END_TIME']:
        return True
    else:
        current_hour = time.localtime(time.time()).tm_hour

        if current_hour > dico['START_TIME'] and current_hour < dico['END_TIME']:
            return True
        else:
            return False
