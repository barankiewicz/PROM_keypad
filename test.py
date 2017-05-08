import time
from CFG import *

def keypadRead():
    single_time = CFG.INTER_DIGIT/8
    for i in range(8):
        press = counter(single_time)
        if not press:
            print('Turning LED no. ' + str(i))
        else:
            print(press)

def counter(dur):
    start = time.time()
    while float(time.time() - start) < dur:
        if float(time.time() - start) < dur/2:
            continue
        else:
            return 'a'

    return False

def time_lockout():
    if START_TIME == END_TIME:
        return True
    else:
        current_hour = time.localtime(time.time()).tm_hour

        if current_hour > START_TIME and current_hour < END_TIME:
            return True
        else:
            return False

print(time_lockout())
