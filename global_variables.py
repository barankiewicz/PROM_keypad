import csv

def read():
    '''
    This function reads the global variables from the csv containing them
    and returns them as a dictionary
    '''
    output = []
    with open('GLOBAL_VARIABLES.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if len(row) == 0:
                continue
            else:
                output.append(tuple(row))
    print(output)
    return {key: int(value) for (key,value) in output}

def read_menu():
    '''
    This function reads the global variables from the csv containing them
    and returns them as a counter dictionary for the menu
    '''
    output = []
    with open('GLOBAL_VARIABLES.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        i = 0
        for row in reader:
            if len(row) == 0:
                continue
            else:
                output.append((i, tuple(row)))
                i += 1
    return {key: value for (key,value) in output}

def write(dico):
    '''
    This function writes back the global variables to the csv file
    '''
    with open('GLOBAL_VARIABLES.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for key in dico:
            writer.writerow([key] + [dico[key]])

print(read())
