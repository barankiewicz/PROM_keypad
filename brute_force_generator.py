
def remove_dup():
    '''
    Removes the duplicates in the file and writes it back to the other one.
    '''
    lines_seen = set() # holds lines already seen
    outfile = open('brute_force.txt', "w")
    for line in open('brute_force2.txt', "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

def add_birthdays():
    '''
    Adds all 4-digit pins to the file in ascending order. PINs are of format DD/MM or MM/DD
    where DD - days of the month (1-31), MM - months (1-12)
    '''
    f = open("brute_force2.txt", 'a')

    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    days =  ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

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

def add_years():
    '''
    Adds all 4-digit pins to the file in ascending order. PINs are of format 19XX.
    '''
    f = open("brute_force2.txt", 'a')
    result = '19'

    for i in range(10):
        for j in range(10):
            result = '19'
            result += str(i)
            result += str(j)
            result += '\n'
            f.write(result)

def add_diagonals():
    '''
    Adds all 4-digit pins to the file in ascending order. PINs are of format XXXX, where X is the same digit.
    '''
    f = open("brute_force2.txt", 'a')

    for i in range(10):
        result = ''
        result += str(i)*4
        result += '\n'
        f.write(result)

def add_1x():
    '''
    Adds all 4-digit pins to the file in ascending order. PINs are of format 1XXX.
    '''
    f = open("brute_force2.txt", 'a')

    for i in range(10):
        for j in range(10):
            for k in range(10):
                result = '1'
                result += str(i)
                result += str(j)
                result += str(k)
                result += '\n'
                f.write(result)

def add_0x():
    '''
    Adds all 4-digit pins to the file in ascending order. PINs are of format 0XXXX.
    '''
    f = open("brute_force2.txt", 'a')

    for i in range(10):
        for j in range(10):
            for k in range(10):
                result = '0'
                result += str(i)
                result += str(j)
                result += str(k)
                result += '\n'
                f.write(result)

def add_random():
    '''
    Adds all 4-digit pins to the file in ascending order
    '''
    f = open("brute_force2.txt", 'a')

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

def generate_bruteforce_file():
    add_diagonals()
    add_years()
    add_1x()
    add_0x()
    add_birthdays()
    add_random()
    remove_dup()

generate_bruteforce_file()
