import adafruit_bno055
import picar
from busio import I2C
from board import SDA, SCL
import time
import sys
import threading
import datetime

i2c = I2C(SCL, SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
# euler = yaw-pitch-roll
# 0 - 180 = right
# 360 - 180 = left

front_wheels = picar.front_wheels.Front_Wheels(debug=True, channel=15)
front_wheels.debug = False
front_wheels.wheel.setup()
front_wheels._angle['straight'] = 90
#front_wheels.turn(70) # min 70, max 120
front_wheels.turn_straight()
# less than 90 = left, greater than 90 = right

back_wheels = picar.back_wheels.Back_Wheels(debug=False, bus_number=1, db="config")
back_wheels.debug = False

class straightThread(threading.Thread):
    def __init__(self, sensor, front_wheels, back_wheels, speed, threshold):
        threading.Thread.__init__(self)
        self.sensor = sensor
        self.front_wheels = front_wheels
        self.back_wheels = back_wheels
        self.speed = speed
        self.turn_stop = False
        self.threshold = threshold
    
    def go_straight(self, x):
        print("Adjusting", x)
        self.front_wheels.turn(90-x)
        while self.turn_stop == False:
            time.sleep(0.05)
            x = self.get_angle()
            if x:
                print(x)
                self.front_wheels.turn(90-x)
                if abs(x) < 5:
                    # Let it go for a while before making straight
                    time.sleep(0.5)
                    break
        print('Done adjusting', x)
        self.front_wheels.turn_straight()
            
    def get_angle(self):
        x = self.sensor.euler[0]
        if x:
            x = x % 360
            if x > 177 and x < 187:
                x = 180
            elif x > 180:
                x = x-360
            return x
        return None
    
    def run(self):
        self.front_wheels.turn_straight()
        self.back_wheels.speed = self.speed
        while self.turn_stop == False:
            x = self.get_angle()
            if x:
                print(x)
                if abs(x) > self.threshold:
                    print("Adjusting")
                    self.front_wheels.turn(90-x)
                    #self.go_straight(x)
            time.sleep(0.1)
    
    def stop(self):
        self.turn_stop = True
        self.join()
        self.front_wheels.turn_straight()
        self.back_wheels.speed = 0
        self.back_wheels.stop()
        print(self.get_angle())
'''
sensor = adafruit_bno055.BNO055_I2C(i2c)
straight_thread = straightThread(sensor, front_wheels, back_wheels, 50)
straight_thread.start()
time.sleep(3)
straight_thread.stop()
'''

def set_default():
    front_wheels.turn_straight()
    back_wheels.speed = 0
    back_wheels.stop()

def turn_by_angle(direction, angle, speed=40, angle_of_servo=30, back_wheels=back_wheels, front_wheels=front_wheels):
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    back_wheels.speed = speed
    if direction == "right":
        front_wheels.turn(90+angle_of_servo)
        euler = sensor.euler[0]
        while (euler == None or euler < angle) or euler > 355:
            print(euler)
            time.sleep(0.01)
            euler = sensor.euler[0]
            if euler == None:
                euler = 0
    else:
        front_wheels.turn(90-angle_of_servo)
        euler = sensor.euler[0]
        while (euler == None or euler > 360-angle) or euler < 95:
            print(euler)
            time.sleep(0.01)
            euler = sensor.euler[0]
            if euler == None:
                euler = 0
    set_default()
    return sensor

def go_straight_time(speed, sleep_time, threshold=10, front_wheels=front_wheels, back_wheels=back_wheels):
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    straight_thread = straightThread(sensor, front_wheels, back_wheels, speed, threshold)
    straight_thread.start()
    time.sleep(sleep_time)
    straight_thread.stop()
    set_default()
    return sensor

try:
    #'''
    while True:
        turn_by_angle("right", 90)
        go_straight_time(40, 5)
        turn_by_angle("right", 90)
        go_straight_time(40, 5)
        turn_by_angle("right", 90)
        go_straight_time(40, 5)
        turn_by_angle("right", 90)
        go_straight_time(40, 5)
        time.sleep(1)
        #'''
    go_straight_time(40, 20, threshold=4)
except:
    print("except:", sys.exc_info())
    set_default()
