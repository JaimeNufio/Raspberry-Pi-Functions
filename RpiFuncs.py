import RPi.GPIO as io;
import time;

def setupOut(outputs):
    for out in outputs:
        for subout in out:
            io.setup(subout,io.OUT);
    motorOff(outputs);

def setupIn(inputs):
    for inp in inputs:
        for subinp in inp:
            io.setup(subinp,io.IN);

def motorOff(pair):
    for inp in pair:
        io.output(inp,0);

def initialize(out,inp):
    io.setmode(io.BCM);
    setupOut(out)
    setupIn(inp)

def end():
    #io.stop()
    io.cleanup()

def motorOn(pair,direction):
    alpha = pair[0]
    beta = pair[1]
    
    if direction:
        io.output(alpha,io.HIGH)
        io.output(beta,io.LOW)
    else:
        io.output(beta,io.HIGH)
        io.output(alpha,io.LOW)
        
def blinkMotor(pair,duration,direction):
    alpha = pair[0]
    beta = pair[1]
    motorOn(pair,direction)
    printStates(pair)
    time.sleep(duration);
    motorOff(pair);

def printStates(pair):
    for p in range(len(pair)):
        print("Input "+str(p)+": ",io.input(pair[p]))
