import time
from data_bus import *
from CFG import *

def play_note(note, dur):
    '''
    EASTER EGG
    '''
    pi_to_key()
    notes = {
    'G4': float(1/392.00),
    'D4': float(1/293.66),
    'D5': float(1/587.33),
    'C5': float(1/523.25),
    'B4': float(1/493.88),
    'A4': float(1/440.00),
    'G5': float(1/783.99)
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
