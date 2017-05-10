import sys, time

def led_display(word):
    '''
    This function implements the 'LED Display' software functionality.
    It takes a string as an input and prints it in the console in a way that
    shows only the last digit of the argument. Then after the fade-out time
    it turns the whole string into a string of just *'s.
    '''
    sys.stdout.write("\r%s%s" % ('*'*(len(word)-1), word[-1]))
    sys.stdout.flush()
    time.sleep(0.3)
    sys.stdout.write("\r%s" % ('*'*len(word)))
    sys.stdout.flush()
