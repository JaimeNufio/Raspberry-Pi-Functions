import RPi.GPIO as io
import RpiFuncs as Rf
import pygame
import random
import time


motor1 = [17,27]
motor2 = [5,6]
motor3 = [23,24]
outputs = [motor1,motor2,motor3]
timedir = .1
states = [False,False,False] 

def changeState(motorPos,state):
    global states
    states[motorPos-1] = state


Rf.initialize(outputs,[])

pygame.init()
pygame.display.set_mode((1, 1))
running = True
active = True

try:
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    changeState(2,True)    
                    Rf.motorOn(motor2,True);
                if event.key == pygame.K_w:
                    changeState(2,False)
                    Rf.motorOff(motor2);
                if event.key == pygame.K_a:
                    changeState(1,True)    
                    Rf.motorOn(motor1,True);
                if event.key == pygame.K_s:
                    changeState(1,False)
                    Rf.motorOff(motor1);
                if event.key == pygame.K_z:
                    changeState(3,True)
                    Rf.motorOn(motor3,True);
                if event.key == pygame.K_x:
                    changeState(3,False)
                    Rf.motorOff(motor3);
                if event.key == pygame.K_p:
                    states = [False,False,False]
                    Rf.motorOff(motor1);Rf.motorOff(motor2);Rf.motorOff(motor3)
                    active = False
        print(states)

except KeyboardInterrupt:
    pass

Rf.motorOff(motor1)
Rf.motorOff(motor2)
Rf.motorOff(motor3)
Rf.end()

