def pi2key():
    GPIO.setmode(GPIO.BCM)
    inputs = (9, 10, 11)
    controls = (14,15) #list of control wires
    GPIO.setup(controls, GPIO.OUT)
    GPIO.output(14, True) #disable LOAD
    GPIO.output(15, False) #enable OUTPUT-ENABLE
    time.sleep(0.01)
    GPIO.setup(inputs, GPIO.OUT)

def key2pi():
    GPIO.setmode(GPIO.BCM)
    inputs = (9, 10, 11)
    controls = (14,15) #list of control wires
    GPIO.setup(controls, GPIO.OUT)
    GPIO.output(14, False) #disable LOAD
    GPIO.output(15, True) #enable OUTPUT-ENABLE
    time.sleep(0.01)
    GPIO.setup(inputs, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    # GPIO.setup(inputs, GPIO.IN)
