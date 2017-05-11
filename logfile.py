import csv, time

def logtime_start():
    '''Logs the start of the system in log.csv'''
    with open('log.csv', 'a') as csvfile:
        log = csv.writer(csvfile, delimiter = ' ')
        log.writerow(['Started the lock: '] +
        [time.gmtime(time.time()).tm_year] +
        [time.gmtime(time.time()).tm_mon] +
        [time.gmtime(time.time()).tm_mday] +
        [time.gmtime(time.time()).tm_hour] +
        [time.gmtime(time.time()).tm_min] +
        [time.gmtime(time.time()).tm_sec])

def logtime_end():
    '''Logs the end of the system in log.csv'''
    with open('log.csv', 'a') as csvfile:
        log = csv.writer(csvfile, delimiter = ' ')
        log.writerow(['Ended the lock: '] +
        [time.gmtime(time.time()).tm_year] +
        [time.gmtime(time.time()).tm_mon] +
        [time.gmtime(time.time()).tm_mday] +
        [time.gmtime(time.time()).tm_hour] +
        [time.gmtime(time.time()).tm_min] +
        [time.gmtime(time.time()).tm_sec])

def logtime(result):
    '''Logs the keypad input in log.csv along with if it was right or wrong'''
    with open('log.csv', 'a') as csvfile:
        log = csv.writer(csvfile, delimiter = ' ')
        log.writerow(
        [time.gmtime(time.time()).tm_year] +
        [time.gmtime(time.time()).tm_mon] +
        [time.gmtime(time.time()).tm_mday] +
        [time.gmtime(time.time()).tm_hour] +
        [time.gmtime(time.time()).tm_min] +
        [time.gmtime(time.time()).tm_sec] +
        [result])
