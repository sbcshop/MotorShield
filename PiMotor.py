#!/usr/bin/python

# Library for PiMotor Shield V1.3
# Developed by: SB Components
# Author: Ankur
# Project: RPi Motor Shield

import RPi.GPIO as GPIO                        #Import GPIO library
import time
from time import sleep
GPIO.setmode(GPIO.BOARD)                       #Set GPIO pin numbering

GPIO.setwarnings(False)

# GPIO of RPi Pins connected with Motor's, LED's and Sensor
Motor1A = 24
Motor1B = 26
Motor2A = 21
Motor2B = 23
Motor3A = 16
Motor3B = 18
Motor4A = 13
Motor4B = 15

    # IR sensor pins
IRsensor1 = 7
IRsensor2 = 12

    # Ultrasonic Sensor
TRIGGER = 29
ECHO    = 31

    # Motor Enable PINS
Motor1EN = 32
Motor2EN = 19
Motor3EN = 22
Motor4EN = 11

    # LED Enable PINS
ArrowLeft = 33
ArrowRight = 35
ArrowForward = 36
ArrowBackward = 37


#Initialize the Motor Shield
def init():     
    # pins connected with motor driver IC Set as Output 
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor3A,GPIO.OUT)
    GPIO.setup(Motor3B,GPIO.OUT)
    GPIO.setup(Motor4A,GPIO.OUT)
    GPIO.setup(Motor4B,GPIO.OUT)

    GPIO.setup(Motor1EN,GPIO.OUT)
    GPIO.setup(Motor2EN,GPIO.OUT)
    GPIO.setup(Motor3EN,GPIO.OUT)
    GPIO.setup(Motor4EN,GPIO.OUT)
    
    # pins connected with arrow LED Set as Output
    GPIO.setup(ArrowLeft,GPIO.OUT)
    GPIO.setup(ArrowRight,GPIO.OUT)
    GPIO.setup(ArrowForward,GPIO.OUT)
    GPIO.setup(ArrowBackward,GPIO.OUT)

    # pins connected with Sensor Set as Input/Output
    GPIO.setup(IRsensor1,GPIO.IN)
    GPIO.setup(IRsensor2,GPIO.IN)
    GPIO.setup(TRIGGER,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    # Initialize all the Pins to LOW ouptut connected with motor and ultrasonic
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor3A, GPIO.LOW)
    GPIO.output(Motor3B, GPIO.LOW)
    GPIO.output(Motor4A, GPIO.LOW)
    GPIO.output(Motor4B, GPIO.LOW)

    GPIO.output(TRIGGER, GPIO.LOW)
    
    # Initialize all the Pins to LOW ouptut connected with LED
    GPIO.output(ArrowLeft, GPIO.LOW)
    GPIO.output(ArrowRight, GPIO.LOW)
    GPIO.output(ArrowForward, GPIO.LOW)
    GPIO.output(ArrowBackward, GPIO.LOW)
     

# LED arrow Indication
def arrow( position, state ):
    if position == 'LEFT': 
        if state == 'ON':       # LEFT arrow LED ON
            GPIO.output(ArrowLeft, GPIO.HIGH)
        if state == 'OFF':                   # LEFT arrow LED OFF
            GPIO.output(ArrowLeft, GPIO.LOW)
        return True
            
    if position == 'RIGHT':
        if state == 'ON':       # RIGHT arrow LED ON
            GPIO.output(ArrowRight, GPIO.HIGH)
        if state == 'OFF':                   # LEFT arrow LED OFF
            GPIO.output(ArrowRight, GPIO.LOW)
        return True
            
    if position == 'FORWARD':
        if state == 'ON':       # FORWARD arrow LED ON
            GPIO.output(ArrowForward, GPIO.HIGH)
        if state == 'OFF':                   # FORWARD arrow LED OFF
            GPIO.output(ArrowForward, GPIO.LOW)    
        return True
    
    if position == 'BACKWARD':
        if state == 'ON':       # BACKWARD arrow LED ON
            GPIO.output(ArrowBackward, GPIO.HIGH)
        if state == 'OFF':                   # BACKWARD arrow LED OFF
            GPIO.output(ArrowBackward, GPIO.LOW)    
        return True
    
    else:
        return False

    

def move(motor,mstate):
    if motor == 'MOTOR1':
        GPIO.output(Motor1EN, GPIO.HIGH)
        if mstate == 'FORWARD':
            GPIO.output(Motor1A, GPIO.LOW)
            GPIO.output(Motor1B, GPIO.HIGH)
            print "Motor1 Moving Forward"
            
        if mstate == 'BACKWARD':
            GPIO.output(Motor1A, GPIO.HIGH)
            GPIO.output(Motor1B, GPIO.LOW)
            print "Motor1 Moving Backward"
            
        if mstate == 'STOP':
            GPIO.output(Motor1EN, GPIO.LOW)
            GPIO.output(Motor1A, GPIO.LOW)
            GPIO.output(Motor1B, GPIO.LOW)
            print "Motor1 STOP"
            
        return True
        
    if motor == 'MOTOR2':
        GPIO.output(Motor2EN, GPIO.HIGH)
        if mstate == 'FORWARD':
            GPIO.output(Motor2A, GPIO.LOW)
            GPIO.output(Motor2B, GPIO.HIGH)
            print "Motor2 Moving Forward"
            
        if mstate == 'BACKWARD':
            GPIO.output(Motor2A, GPIO.HIGH)
            GPIO.output(Motor2B, GPIO.LOW)
            print "Motor2 Moving Backward"
            
        if mstate == 'STOP':
            GPIO.output(Motor2EN, GPIO.LOW)
            GPIO.output(Motor2A, GPIO.LOW)
            GPIO.output(Motor2B, GPIO.LOW)
            print "Motor2 STOP"
            
        return True

    if motor == 'MOTOR3':
        GPIO.output(Motor3EN, GPIO.HIGH)
        if mstate == 'FORWARD':
            GPIO.output(Motor3A, GPIO.LOW)
            GPIO.output(Motor3B, GPIO.HIGH)
            print "Motor3 Moving Forward"
            
        if mstate == 'BACKWARD':
            GPIO.output(Motor3A, GPIO.HIGH)
            GPIO.output(Motor3B, GPIO.LOW)
            print "Motor3 Moving Backward"
            
        if mstate == 'STOP':
            GPIO.output(Motor3EN, GPIO.LOW)
            GPIO.output(Motor3A, GPIO.LOW)
            GPIO.output(Motor3B, GPIO.LOW)
            print "Motor3 STOP"
            
        return True
    
    if motor == 'MOTOR4':
        GPIO.output(Motor4EN, GPIO.HIGH)
        if mstate == 'FORWARD':
            GPIO.output(Motor4A, GPIO.LOW)
            GPIO.output(Motor4B, GPIO.HIGH)
            print "Motor4 Moving Forward"
            
        if mstate == 'BACKWARD':
            GPIO.output(Motor4A, GPIO.HIGH)
            GPIO.output(Motor4B, GPIO.LOW)
            print "Motor4 Moving Backward"
            
        if mstate == 'STOP':
            GPIO.output(Motor4EN, GPIO.LOW)
            GPIO.output(Motor4A, GPIO.LOW)
            GPIO.output(Motor4B, GPIO.LOW)
            print "Motor4 STOP"
            
        return True

    if motor == 'ALL':
        GPIO.output(Motor1EN, GPIO.HIGH)
        GPIO.output(Motor2EN, GPIO.HIGH)
        GPIO.output(Motor3EN, GPIO.HIGH)
        GPIO.output(Motor4EN, GPIO.HIGH)
        
        if mstate == 'FORWARD':
            GPIO.output(Motor1A, GPIO.LOW)
            GPIO.output(Motor1B, GPIO.HIGH)
            GPIO.output(Motor2A, GPIO.LOW)
            GPIO.output(Motor2B, GPIO.HIGH)
            GPIO.output(Motor3A, GPIO.LOW)
            GPIO.output(Motor3B, GPIO.HIGH)
            GPIO.output(Motor4A, GPIO.LOW)
            GPIO.output(Motor4B, GPIO.HIGH)
            print "All Motor Moving Forward"
            
        if mstate == 'BACKWARD':
            GPIO.output(Motor1A, GPIO.HIGH)
            GPIO.output(Motor1B, GPIO.LOW)
            GPIO.output(Motor2A, GPIO.HIGH)
            GPIO.output(Motor2B, GPIO.LOW)
            GPIO.output(Motor3A, GPIO.HIGH)
            GPIO.output(Motor3B, GPIO.LOW)
            GPIO.output(Motor4A, GPIO.HIGH)
            GPIO.output(Motor4B, GPIO.LOW)
            print "All Motor Moving Backward"
            
        if mstate == 'STOP':
            GPIO.output(Motor1EN, GPIO.LOW)
            GPIO.output(Motor2EN, GPIO.LOW)
            GPIO.output(Motor3EN, GPIO.LOW)
            GPIO.output(Motor4EN, GPIO.LOW)
            GPIO.output(Motor1A, GPIO.LOW)
            GPIO.output(Motor1B, GPIO.LOW)
            GPIO.output(Motor1A, GPIO.LOW)
            GPIO.output(Motor1B, GPIO.LOW)
            GPIO.output(Motor1A, GPIO.LOW)
            GPIO.output(Motor1B, GPIO.LOW)
            GPIO.output(Motor1A, GPIO.LOW)
            GPIO.output(Motor1B, GPIO.LOW)
            print "All STOP"
            
        return True

    else:
        return False


# Read IR sensor 1 Input
def readIR1():
    input_state = GPIO.input(IRsensor1)
    if input_state == True:
        print "Sensor 1: Object Detected"
    return input_state

# Read IR sensor 2 Input
def readIR2():
    input_state = GPIO.input(IRsensor2)
    if input_state == True:
        print "Sensor 2: Object Detected"
    return input_state

# Ultrasonic Sensor read distance
def distance():
    time.sleep(0.333)
    GPIO.output(TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)
    start = time.time()
  
    while GPIO.input(ECHO)==0:
        start = time.time()

    while GPIO.input(ECHO)==1:
        stop = time.time()

    elapsed = stop-start
    measure = (elapsed * 34300)/2
    print "Distance : %.1f" % measure
    return measure
    
