import PiMotor

import time
import sys
import threading
import datetime
import RPi.GPIO as GPIO
from math import *
#from ultrasonic_thread import ultra

import adafruit_bno055
import board

i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

'''
print(sensor.temperature)
print(sensor.euler)
print(sensor.gravity)
'''
# GPIO.setmode(GPIO.BCM) 
# GPIO.setwarnings(False)

m1 = PiMotor.Motor("MOTOR1",2) # Left Wheel: Reverse is forward
m2 = PiMotor.Motor("MOTOR2",1) # Right Wheel: forward is forward

class straightThread(threading.Thread):
    def __init__(self, sensor, left_wheels, right_wheels, speed, threshold):
        threading.Thread.__init__(self)
        self.sensor = sensor
        self.left_wheels = left_wheels
        self.right_wheels = right_wheels
        self.speed = speed
        self.turn_stop = False
        self.threshold = threshold
            
    def get_angle(self):
        x = self.sensor.euler[0]
        if x:
            x = x % 360
            if x > 180:
                x = x-360
            return x
        return None
    
    def run(self):
        print("Angles before move:", self.sensor.euler[0], self.sensor.euler[0], self.sensor.euler[0], self.sensor.euler[0], self.sensor.euler[0])
        num_times_corrected= 0
        self.left_wheels.forward(self.speed-10)
        self.right_wheels.forward(self.speed)
        while self.turn_stop == False:
            x = self.get_angle()
            if x:
                if abs(x) > self.threshold:
                    num_times_corrected += 1
                    self.left_wheels.forward(self.speed-round(x/2.5))
                    self.right_wheels.forward(self.speed+round(x/2.5))
            time.sleep(0.1)
        print("Angle after move:", self.sensor.euler[0])
        print("Times Corrected:", num_times_corrected)
    
    def stop(self):
        self.turn_stop = True
        self.join()
        self.left_wheels.stop()
        self.right_wheels.stop()
        print(self.get_angle())

def go_straight(speed, left_wheels=m1, right_wheels=m2, threshold=10):
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    straight_thread = straightThread(sensor, left_wheels, right_wheels, speed, threshold)
    straight_thread.start()
    return sensor, straight_thread
# This function starts the straightThread and to stop it going forward call straight_thread.stop()

def turn_by_angle(direction, angle, speed=40, m1=m1, m2=m2):
    angle-=10
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    if direction == "r":
        m1.forward(speed-10)
        m2.reverse(speed)
        euler = sensor.euler[0]
        print(euler)
        while (euler == None or euler < angle) or euler > 355:
            #print(euler)
            time.sleep(0.01)
            euler = sensor.euler[0]
            if euler == None:
                euler = 0
    else:
        m1.reverse(speed-10)
        m2.forward(speed)
        euler = sensor.euler[0]
        while (euler == None or euler > 360-angle) or euler < 95:
            #print(euler)
            time.sleep(0.01)
            euler = sensor.euler[0]
            if euler == None:
                euler = 0
    m1.stop()
    m2.stop()
    print(euler)
    return sensor


try:
    while True:
        thing_2_do = input("f, b, l, r: ")
        if thing_2_do == 'f':
            forward_time = input("How long: ")
            new_sensor, thread = go_straight(50)
            time.sleep(int(forward_time))
            thread.stop()
            sensor = new_sensor
        elif thing_2_do == 'b':
            m1.reverse(45)
            m2.reverse(50)
            time.sleep(3)
            m1.stop()
            m2.stop()
        elif thing_2_do == 'l':
            angle = input("Angle: ")
            turn_by_angle('l', int(angle))
        elif thing_2_do == 'r':
            angle = input("Angle: ")
            turn_by_angle('r', int(angle))
except Exception as e:
    print('ERROR:', e)
finally:
    m1.stop()
    m2.stop()
    ultra.stop()
    GPIO.cleanup()

'''

ultra = ultra()
ultra.start()
new_sensor, thread = go_straight(50)
try:
	while True:
		if ultra.get_dist() < 2:
			print("Move Away")
except Exception as e:
	print("FAILURE:", e)
finally:
    m1.stop()
    m2.stop()
    ultra.stop()
    GPIO.cleanup()
'''
