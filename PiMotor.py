#!/usr/bin/python

# Library for PiMotor Shield V2
# Developed by: SB Components
# Project: RPi Motor Shield

import RPi.GPIO as GPIO                        #Import GPIO library
import time
from time import sleep
GPIO.setmode(GPIO.BOARD)                       #Set GPIO pin numbering

GPIO.setwarnings(False)

class Motor:
    ''' Class to handle interaction with the motor pins
    Supports redefinition of "forward" and "backward" depending on how motors are connected
    Use the supplied Motorshieldtest module to test the correct configuration for your project.
    
    Arguments:
    motor = string motor pin label (i.e. "MOTOR1","MOTOR2","MOTOR3","MOTOR4") identifying the pins to which
            the motor is connected.
    config = int defining which pins control "forward" and "backward" movement.
    '''
    motorpins = {"MOTOR4":{"config":{1:{"e":32,"f":24,"r":26},2:{"e":32,"f":26,"r":24}},"arrow":1},
                 "MOTOR3":{"config":{1:{"e":19,"f":21,"r":23},2:{"e":19,"f":23,"r":21}}, "arrow":2},
                 "MOTOR2":{"config":{1:{"e":22,"f":16,"r":18},2:{"e":22,"f":18,"r":16}}, "arrow":3},
                 "MOTOR1":{"config":{1:{"e":11,"f":15,"r":13},2:{"e":11,"f":13,"r":15}},"arrow":4}}
    
    def __init__(self, motor, config):
        self.testMode = False
        self.arrow = Arrow(self.motorpins[motor]["arrow"])
        self.pins = self.motorpins[motor]["config"][config]
        GPIO.setup(self.pins['e'],GPIO.OUT)
        GPIO.setup(self.pins['f'],GPIO.OUT)
        GPIO.setup(self.pins['r'],GPIO.OUT)
        self.PWM = GPIO.PWM(self.pins['e'], 50)  # 50Hz frequency
        self.PWM.start(0)
        GPIO.output(self.pins['e'],GPIO.HIGH)
        GPIO.output(self.pins['f'],GPIO.LOW)
        GPIO.output(self.pins['r'],GPIO.LOW)

    def test(self, state):
        ''' Puts the motor into test mode
        When in test mode the Arrow associated with the motor receives power on "forward"
        rather than the motor. Useful when testing your code. 
        
        Arguments:
        state = boolean
        '''
        self.testMode = state

    def forward(self, speed):
        ''' Starts the motor turning in its configured "forward" direction.

        Arguments:
        speed = Duty Cycle Percentage from 0 to 100.
        0 - stop and 100 - maximum speed
        '''    
        print("Forward")
        if self.testMode:
            self.arrow.on()
        else:
            self.PWM.ChangeDutyCycle(speed)
            GPIO.output(self.pins['f'],GPIO.HIGH)
            GPIO.output(self.pins['r'],GPIO.LOW)

    def reverse(self,speed):
        ''' Starts the motor turning in its configured "reverse" direction.

        Arguments:
        speed = Duty Cycle Percentage from 0 to 100.
        0 - stop and 100 - maximum speed
     '''
        print("Reverse")
        if self.testMode:
            self.arrow.off()
        else:
            self.PWM.ChangeDutyCycle(speed)
            GPIO.output(self.pins['f'],GPIO.LOW)
            GPIO.output(self.pins['r'],GPIO.HIGH)

    def stop(self):
        ''' Stops power to the motor,
     '''
        print("Stop")
        self.arrow.off()
        self.PWM.ChangeDutyCycle(0)
        GPIO.output(self.pins['f'],GPIO.LOW)
        GPIO.output(self.pins['r'],GPIO.LOW)

    def speed(self):
        ''' Control Speed of Motor,
     '''

class LinkedMotors:
    ''' Links 2 or more motors together as a set.
    
        This allows a single command to be used to control a linked set of motors
        e.g. For a 4x wheel vehicle this allows a single command to make all 4 wheels go forward.
        Starts the motor turning in its configured "forward" direction.
        
        Arguments:
        *motors = a list of Motor objects
     '''
    def __init__(self, *motors):
        self.motor = []
        for i in motors:
            print(i.pins)
            self.motor.append(i)

    def forward(self,speed):
        ''' Starts the motor turning in its configured "forward" direction.

        Arguments:
        speed = Duty Cycle Percentage from 0 to 100.
        0 - stop and 100 - maximum speed 
     '''
        for i in range(len(self.motor)):
            self.motor[i].forward(speed)

    def reverse(self,speed):
        ''' Starts the motor turning in its configured "reverse" direction.

        Arguments:
        speed = Duty Cycle Percentage from 0 to 100.
        0 - stop and 100 - maximum speed
     '''
        for i in range(len(self.motor)):
            self.motor[i].reverse(speed)

    def stop(self):
        ''' Stops power to the motor,
     '''
        for i in range(len(self.motor)):
            self.motor[i].stop()



class Stepper:
    ''' Defines stepper motor pins on the MotorShield
    
        Arguments:
        motor = stepper motor
    '''
    
    stepperpins = {"STEPPER1":{"en1":11, "en2":22, "c1":13,"c2":15, "c3":18, "c4":16},
                   "STEPPER2":{"en1":19, "en2":32, "c1":21,"c2":23, "c3":24, "c4":26}}
                  
    def __init__(self, motor):
        self.config = self.stepperpins[motor]
        GPIO.setup(self.config["en1"],GPIO.OUT)
        GPIO.setup(self.config["en2"],GPIO.OUT)
        GPIO.setup(self.config["c1"],GPIO.OUT)
        GPIO.setup(self.config["c2"],GPIO.OUT)
        GPIO.setup(self.config["c3"],GPIO.OUT)
        GPIO.setup(self.config["c4"],GPIO.OUT)
        
        GPIO.output(self.config["en1"],GPIO.HIGH)
        GPIO.output(self.config["en2"],GPIO.HIGH)
        GPIO.output(self.config["c1"],GPIO.LOW)
        GPIO.output(self.config["c2"],GPIO.LOW)
        GPIO.output(self.config["c3"],GPIO.LOW)
        GPIO.output(self.config["c4"],GPIO.LOW)

    ''' Set steps of Stepper Motor
    
        Arguments:
        w1,w2,w3,w4 = Wire of Stepper Motor
    '''
    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.config["c1"], w1)
        GPIO.output(self.config["c2"], w2)
        GPIO.output(self.config["c3"], w3)
        GPIO.output(self.config["c4"], w4)

    ''' Rotate Stepper motor in forward direction
    
        Arguments:
        delay = time between steps in miliseconds
        steps = Number of Steps
    '''
    def forward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)

    ''' Rotate Stepper motor in backward direction
    
        Arguments:
        delay = time between steps
        steps = Number of Steps
    '''
    def backward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)

    def stop(self):
        ''' Stops power to the motor,
     '''
        print("Stop Stepper Motor")
        GPIO.output(self.config['c1'],GPIO.LOW)
        GPIO.output(self.config['c2'],GPIO.LOW)
        GPIO.output(self.config['c3'],GPIO.LOW)
        GPIO.output(self.config['c4'],GPIO.LOW)
        


class Sensor:
    ''' Defines a sensor connected to the sensor pins on the MotorShield
    
        Arguments:
        sensortype = string identifying which sensor is being configured.
            i.e. "IR1", "IR2", "ULTRASONIC"
        boundary = an integer specifying the minimum distance at which the sensor
            will return a Triggered response of True. 
    '''
    Triggered = False
    def iRCheck(self):
        input_state = GPIO.input(self.config["echo"])
        if input_state == True:
            print("Sensor 2: Object Detected")
            self.Triggered = True
        else:
            self.Triggered = False

    def sonicCheck(self):
        print("SonicCheck has been triggered")
        time.sleep(0.333)
        GPIO.output(self.config["trigger"], True)
        time.sleep(0.00001)
        GPIO.output(self.config["trigger"], False)
        start = time.time()
        while GPIO.input(self.config["echo"])==0:
            start = time.time()
        while GPIO.input(self.config["echo"])==1:
            stop = time.time()
        elapsed = stop-start
        measure = (elapsed * 34300)/2
        self.lastRead = measure
        if self.boundary > measure:
            print("Boundary breached")
            print(self.boundary)
            print(measure)
            self.Triggered = True
        else:
            self.Triggered = False
        
    sensorpins = {"IR1":{"echo":7, "check":iRCheck}, "IR2":{"echo":12, "check":iRCheck},
                  "ULTRASONIC":{"trigger":29, "echo": 31, "check":sonicCheck}}

    def trigger(self):
        ''' Executes the relevant routine that activates and takes a reading from the specified sensor.
    
        If the specified "boundary" has been breached the Sensor's Triggered attribute gets set to True.
    ''' 
        self.config["check"](self)
        print("Trigger Called")

    def __init__(self, sensortype, boundary):
        self.config = self.sensorpins[sensortype]
        self.boundary = boundary
        self.lastRead = 0
        if "trigger" in self.config:
            print("trigger")
            GPIO.setup(self.config["trigger"],GPIO.OUT)
        GPIO.setup(self.config["echo"],GPIO.IN) 

class Arrow():
    ''' Defines an object for controlling one of the LED arrows on the Motorshield.
    
        Arguments:
        which = integer label for each arrow. The arrow number if arbitrary starting with:
            1 = Arrow closest to the Motorshield's power pins and running clockwise round the board
            ...
            4 = Arrow closest to the motor pins.
    '''
    arrowpins={1:33,2:35,3:37,4:36}

    def __init__(self, which):
        self.pin = self.arrowpins[which]
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin,GPIO.LOW)
