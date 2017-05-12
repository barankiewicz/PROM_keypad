import time
from data_bus import *
from CFG import *

def play_note(note, dur):
    '''
    EASTER EGG
    '''
    pi_to_key()
    notes = {
    'A3': float(1/220.00),
    'Bb3': float(1/233.08),
    'C4': float(1/261.63),
    'D4': float(1/293.66),
    'E4': float(1/329.63),
    'F4': float(1/349.23),
    'G4': float(1/392.00),
    'Ab4': float(1/415.30),
    'A4': float(1/440.00),
    'Bb4': float(1/466.16),
    'B4': float(1/493.88),
    'C5': float(1/523.25),
    'Db5': float(1/554.37),
    'D5': float(1/587.33),
    'Eb5': float(1/622.25),
    'E5': float(1/659.25),
    'F5': float(1/698.46),
    'Gb5': float(1/739.99),
    'G5': float(1/783.99),
    'A5': float(1/880.00),
    'B5': float(1/987.77),
    'C6': float(1/1046.50)
    }
    start = time.time()
    while float(time.time() - start) < dur:
        GPIO.output(DATA0, 1)  #MSB
        GPIO.output(DATA1, 1)
        GPIO.output(DATA2, 0) #LSB
        time.sleep(notes[note])
        GPIO.output(DATA0, 0)  #MSB
        GPIO.output(DATA1, 0)
        GPIO.output(DATA2, 0) #LSB
        time.sleep(notes[note])
    return

def star_wars():
#   crotchet = 0.6

    play_note('D4', 0.2)
    play_note('D4', 0.2)
    play_note('D4', 0.2)

    play_note('G4', 1.2)
    play_note('D5', 1.2)

    play_note('C5', 0.2)
    play_note('B4', 0.2)
    play_note('A4', 0.2)
    play_note('G5', 1.2)
    play_note('D5', 0.6)

    play_note('C5', 0.2)
    play_note('B4', 0.2)
    play_note('A4', 0.2)
    play_note('G5', 1.2)
    play_note('D5', 0.6)

    play_note('C5', 0.2)
    play_note('B4', 0.2)
    play_note('C5', 0.2)
    play_note('A4', 1.8)

def careless_whisper():
    #   crotchet = 0.8

    play_note('F4', 0.1)
    play_note('G4', 0.1)
    play_note('A4', 0.1)
    play_note('C5', 0.1)

    play_note('E5', 0.4)
    play_note('D5', 0.2)
    play_note('A4', 0.4)
    play_note('F4', 0.4)
    play_note('E5', 0.6)
    play_note('D5', 0.2)
    play_note('A4', 0.4)
    play_note('F4', 0.4)

    time.sleep(0.2)

    play_note('C5', 0.4)
    play_note('Bb4', 0.2)
    play_note('F4', 0.4)
    play_note('D4', 0.4)
    play_note('C5', 0.6)
    play_note('Bb4', 0.2)
    play_note('F4', 0.6)

    time.sleep(0.4)

    play_note('Bb4', 0.4)
    play_note('A4', 0.2)
    play_note('F4', 0.4)
    play_note('D4', 0.4)
    play_note('Bb3', 1.8)

    play_note('A3', 0.4)
    play_note('Bb3', 0.4)
    play_note('C4', 0.4)
    play_note('D4', 0.4)
    play_note('E4', 0.4)
    play_note('F4', 0.4)
    play_note('G4', 0.4)
    play_note('A4', 0.4)

def super_mario1():
    #   crotchet = 0.6

    play_note('E5', 0.15)
    play_note('E5', 0.15)
    time.sleep(0.15)
    play_note('E5', 0.15)
    time.sleep(0.15)
    play_note('C5', 0.15)
    play_note('E5', 0.15)
    time.sleep(0.15)
    play_note('G5', 0.15)
    time.sleep(0.45)
    play_note('G4', 0.15)
    time.sleep(0.45)

    for x in range(2):
        play_note('C5', 0.15)
        time.sleep(0.3)
        play_note('G4', 0.15)
        time.sleep(0.3)
        play_note('E4', 0.15)
        time.sleep(0.3)
        play_note('A4', 0.15)
        time.sleep(0.15)
        play_note('B4', 0.15)
        time.sleep(0.15)
        play_note('Bb4', 0.15)
        play_note('A4', 0.15)
        time.sleep(0.15)

        play_note('G4', 0.2)
        play_note('E5', 0.2)
        play_note('G5', 0.2)
        play_note('A5', 0.15)
        time.sleep(0.15)
        play_note('F5', 0.15)
        play_note('G5', 0.15)
        time.sleep(0.15)
        play_note('E5', 0.15)
        time.sleep(0.15)
        play_note('C5', 0.15)
        play_note('D5', 0.15)
        play_note('B4', 0.15)
        time.sleep(0.3)

def super_mario2():
    # crotchet = 0.3

    play_note('G5', 0.1)
    play_note('Gb5', 0.1)
    time.sleep(0.1)
    play_note('F5', 0.1)
    play_note('D5', 0.1)
    time.sleep(0.1)
    play_note('B4', 0.1)
    play_note('A4', 0.1)
    time.sleep(0.1)
    play_note('Ab4', 0.1)
    play_note('G4', 0.2)
    time.sleep(0.1)
    play_note('G5', 0.2)
    time.sleep(0.1)
    play_note('G4', 0.3)
    time.sleep(0.3)

    play_note('G5', 0.1)
    time.sleep(0.1)
    play_note('C5', 0.1)
    play_note('E5', 0.1)
    time.sleep(0.1)
    play_note('G5', 0.3)
    play_note('C5', 0.1)
    play_note('E5', 0.1)
    time.sleep(0.1)
    play_note('G5', 0.1)
    play_note('B4', 0.1)
    play_note('Eb5', 0.1)
    play_note('G5', 0.1)
    play_note('B5', 0.1)
    time.sleep(0.1)
    play_note('A5', 0.7)

    play_note('G5', 0.1)
    time.sleep(0.1)
    play_note('Bb4', 0.1)
    play_note('D5', 0.1)
    time.sleep(0.1)
    play_note('G5', 0.3)
    play_note('Bb4', 0.1)
    play_note('D5', 0.1)
    time.sleep(0.1)
    play_note('G5', 0.1)
    play_note('Db5', 0.1)
    play_note('E5', 0.1)
    play_note('G5', 0.1)
    play_note('B5', 0.1)
    time.sleep(0.1)
    play_note('A5', 0.6)

    play_note('B5', 0.1)
    play_note('C6', 0.1)
    time.sleep(0.1)
    play_note('B5', 0.1)
    play_note('C6', 0.1)
    time.sleep(0.1)
    play_note('A5', 0.3)
    play_note('C6', 0.1)
    play_note('B5', 0.1)
    time.sleep(0.1)
    play_note('A5', 0.1)
    play_note('G5', 0.1)
    time.sleep(0.1)
    play_note('Gb5', 0.1)
    play_note('G5', 0.1)
    time.sleep(0.1)
    play_note('E5', 0.3)
    play_note('Db5', 0.1)
    play_note('D5', 0.1)
    time.sleep(0.1)
    play_note('E5', 0.1)
    play_note('F5', 0.1)
    time.sleep(0.1)
    play_note('E5', 0.1)
    play_note('F5', 0.1)
    time.sleep(0.1)
    play_note('B4', 0.3)
    play_note('E5', 0.1)
    play_note('D5', 0.1)
    time.sleep(0.1)
    play_note('C5', 0.7)
