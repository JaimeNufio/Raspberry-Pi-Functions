import RPi.GPIO as io
import time
import random
import RpiFuncs as Rf

motor1 = [17,27]
outputs = [motor1]

Rf.initialize(motor1,[])

try:

    while True:
        Rf.blinkMotor(motor1,random.randrange(5,10),False)
        Rf.printStates(motor1)
        Rf.blinkMotor(motor1,random.randrange(5,10),True)
        Rf.printStates(motor1)

except KeyboardInterrupt:
    pass

Rf.motorOff(motor1)
Rf.end()
