import RPi.GPIO as GPIO
import time

import PiMotor

GPIO.setwarnings(False)

TRIG = 29
ECHO = 31

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)

def stop():
    print("Robot Stop ")
    al.off()
    af.off()
    ar.off()
    motorAll.stop()
    time.sleep(2)

def forward():
    print("Robot Moving Forward ")
    af.on()
    motorAll.forward(100)
    time.sleep(2)

def back():
    print("Robot Moving Backward ")
    af.off()
    ab.on()
    motorAll.reverse(100)
    time.sleep(2)

def left():
    print("Robot Moving Left ")
    ab.off()
    al.on()
    m1.stop()
    m2.stop()
    m3.forward(100)
    m4.forward(100)
    time.sleep(2)

def right():
    print("Robot Moving Right ")
    ar.on()
    al.off()
    m1.forward(100)
    m2.forward(100)
    m3.stop()
    m4.stop()
    time.sleep(2)

stop()
count=0
while True:
 i=0
 avgDistance=0
 for i in range(5):
    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start

        distance = (pulse_duration * 34300)/2
        distance = round(distance,2)
        avgDistance=avgDistance+distance

        avgDistance=avgDistance/5
        print(avgDistance)

    if avgDistance < 20:
        count=count+1
        stop()
        time.sleep(1)
        back()
        time.sleep(2)
        if (count%4 ==1):
            right()

        else:
            forward()
