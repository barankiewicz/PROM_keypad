from i2c_lockpick import *

def brute_force():
    '''
    This function implements the brute force attack technique.
    It reads the order of the passwords it should check from the file 'brute_force.txt'.
    The file was created with optimization of cracking times in mind.
    The first 20 lines are the 20 most common PINs according to the study held by:
    http://datagenetics.com/blog/september32012/index.html
    For the full discussion on how I improved the cracking times, please refer to my
    individual log I submitted with the code.
    According to the article, those 20 PINs make up for over 25% of all PINs being used
    in the world right now. So that should be a VERY significant speed up over just checking
    the combinations randomly.
    The next 456 lines are lines in the format of DDMM/MMDD, where DD - day of the month,
    MM - month. According to the article mentioned above, people tend to use PINs
    in this format very often.
    The rest of the files are the passwords generated randomly in a way so that there are
    no duplicates.
    '''

    f = open('brute_force.txt', 'r')

    for row in f:
        password = row
        password = password.strip('\n')

        for letter in password:
            idle(0.5)
            drive_char(letter)
            idle(0.5)

        time.sleep(0.2)
        led = check_red()
        if led == False:
            continue
        else:
            print(row)
            return row
