from random import randint
from collections import OrderedDict

def remove_duplicates():
    lines_seen = [] # holds lines already seen
    outfile = open('brute_force2.txt', "w")
    for line in open('brute_force.txt', "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.append(line)
    outfile.close()


def add_birthdays():
    f = open("brute_force.txt", 'a')

    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    days =  ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    f.write('\n')

    for i in range(len(months)):
        for j in range(len(days)):
            result = ''
            result += months[i]
            result += days[j]
            result += '\n'
            f.write(result)

    for i in range(len(days)):
        for j in range(len(months)):
            result = ''
            result += days[i]
            result += months[j]
            result += '\n'
            f.write(result)

    f.close()

def read_file():
    f = open("brute_force.txt", 'r')

    result = []

    for row in f:
        result.append(row)
    return result

def file_len():
    with open("brute_force.txt", 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def add_random():
    f = open("brute_force.txt", 'a')

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    result = ''
                    result += str(i)
                    result += str(j)
                    result += str(k)
                    result += str(l)
                    result += '\n'
                    f.write(result)

remove_duplicates()
