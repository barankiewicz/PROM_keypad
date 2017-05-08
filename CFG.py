INTER_DIGIT = 3

########### MAXIMUM TRY LOCKOUT #

MAXIMUM_TRIES = 0
TIMEOUT = 5

########### TIME LOCKOUT #######

START_TIME = 0
END_TIME = 0

########### PINS ###############

LOAD = 17
OUTPUT_ENABLE = 15
CONTROLS = (LOAD, OUTPUT_ENABLE)
DATABUS = (9, 10, 11)
DATA0 = DATABUS[0]
DATA1 = DATABUS[1]
DATA2 = DATABUS[2]

###############################

#a matrix representing the keypad
MATRIX = [
[1, 2, 3, 'A'],
[4, 5, 6, 'B'],
[7, 8, 9, 'C'],
['*', 0, '#', 'D']
]

#a dictionary that maps rows numbers to wire arrangement
MAP = {
0: (0, 0, 0), #000
1: (0, 0, 1),  #001
2: (0, 1, 0),  #010
3: (0, 1, 1)    #011
}

#a dictionary that maps columns numbers to wire arrangement (onehot)
MAP_ONEHOT = {
0: (1, 1, 0),
1: (1, 0, 1),
2: (0, 1, 1)
}
