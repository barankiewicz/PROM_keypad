import time
from CFG import *

def time_lockout():
    if START_TIME == END_TIME:
        return True
    else:
        current_hour = time.localtime(time.time()).tm_hour

        if current_hour > START_TIME and current_hour < END_TIME:
            return True
        else:
            return False
