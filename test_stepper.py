import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)   #Set GPIO pin numbering

GPIO.setwarnings(False)

coil_a  = 13 # M1A
coil_a1 = 15 # M2A
coil_b  = 18 # M1B
coil_b1 = 16 # BM2
 
#  if different then adjust
count = 8
sequence = list(range(0, count))

sequence[0] = [0,1,0,0]
sequence[1] = [0,1,0,1]
sequence[2] = [0,0,0,1]
sequence[3] = [1,0,0,1]
sequence[4] = [1,0,0,0]
sequence[5] = [1,0,1,0]
sequence[6] = [0,0,1,0]
sequence[7] = [0,1,1,0]
 
GPIO.setup(11, GPIO.OUT)# enable pin
GPIO.setup(22, GPIO.OUT)# enable pin

GPIO.output(11,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)

GPIO.setup(coil_a, GPIO.OUT)
GPIO.setup(coil_a1, GPIO.OUT)
GPIO.setup(coil_b, GPIO.OUT)
GPIO.setup(coil_b1, GPIO.OUT)
 
 
def Step(w1, w2, w3, w4):
    GPIO.output(coil_a, w1)
    GPIO.output(coil_a1, w2)
    GPIO.output(coil_b, w3)
    GPIO.output(coil_b1, w4)

delay = int(input("Delay in ms = "))/1000.0 # time in milli second
steps = int(input("steps forward = "))
for i in range(steps):
        for j in range(count):
            Step(sequence[j][0], sequence[j][1], sequence[j][2], sequence[j][3])
            time.sleep(delay)


steps = int(input("steps backward = "))       
for i in range(steps):
        for j in reversed(range(count)):
            Step(sequence[j][0], sequence[j][1], sequence[j][2], sequence[j][3])
            time.sleep(delay)

