import PiMotor
import time
import RPi.GPIO as GPIO
import threading

# GPIO.setmode(GPIO.BOARD)

sequence = [
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
    [1,0,0,1]
   ]
delay = 0.001
steps = 512

rightM = PiMotor.Stepper("STEPPER1")
leftM = PiMotor.Stepper("STEPPER2")
rightM.setSequence(sequence)
leftM.setSequence(sequence)

class motorThread(threading.Thread):
    def __init__(self, motor, delay, steps, direc):
        threading.Thread.__init__(self)
        self.motor = motor
        self.direc = direc
        self.delay = delay
        self.steps = steps
        
    def run(self):
        if self.direc == "f":
            self.motor.forward(self.delay, self.steps)
        else:
            self.motor.backward(self.delay, self.steps)

def move(motor1, motor2, delay, steps, direc1, direc2):
    thread1 = motorThread(motor1, delay, steps, direc1)
    thread2 = motorThread(motor2, delay, steps, direc2)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

def forward(motor1, motor2, delay, steps):
    move(motor1, motor2, delay, steps, "f", "b")

def backward(motor1, motor2, delay, steps):
    move(motor1, motor2, delay, steps, "b", "f")

def left(motor1, motor2, delay, steps):
    move(motor1, motor2, delay, steps, "f", "f")

def right(motor1, motor2, delay, steps):
    move(motor1, motor2, delay, steps, "b", "b")

# Rotate Stepper 1 Contiously in forward/backward direction
# Rotating the fastest the motor can go
while True:
    print("forward")
    forward(rightM, leftM, delay, steps)
    time.sleep(0.5)
    print("backward")
    backward(rightM, leftM, delay, steps)
    time.sleep(0.5)
    print("left")
    left(rightM, leftM, delay, steps)
    time.sleep(0.5)
    print("right")
    right(rightM, leftM, delay, steps)
    time.sleep(0.5)
    print("Safe to Terminate")
    time.sleep(5)
