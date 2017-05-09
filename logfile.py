import csv, time

def logtime_start():
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
    with open('log.csv', 'a') as csvfile:
        log = csv.writer(csvfile, delimiter = ' ')
        log.writerow(['Entered combination'] +
        [time.gmtime(time.time()).tm_year] +
        [time.gmtime(time.time()).tm_mon] +
        [time.gmtime(time.time()).tm_mday] +
        [time.gmtime(time.time()).tm_hour] +
        [time.gmtime(time.time()).tm_min] +
        [time.gmtime(time.time()).tm_sec] +
        [result])
