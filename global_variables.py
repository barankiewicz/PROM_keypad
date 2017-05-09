import time
from CFG import *
import csv



def read():
    output = []
    with open('GLOBAL_VARIABLES.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            output.append(tuple(row))
    return {key: int(value) for (key,value) in output}

def write(dico):
    with open('GLOBAL_VARIABLES.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for key in dico:
            writer.writerow([key] + [dico[key]])
