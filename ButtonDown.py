import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)

bttndn = False
timecnt = 0
while True:
    time.sleep(.01)
    if(GPIO.input(27) and not bttndn):
        print("Button Released, was down ",timecnt)
        bttndn=not bttndn
        timecnt=0
    elif (not GPIO.input(27) and bttndn):
        print("Button Down")
        bttndn = not bttndn

    if (bttndn):
        timecnt+=.01
        
GPIO.cleanup()
