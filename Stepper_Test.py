import PiMotor
import time
import RPi.GPIO as GPIO

m1 = PiMotor.Stepper("STEPPER1")

# Rotate Stepper 1 Contiously in forward/backward direction
try:
    while True:
        m1.forward(0.1,10)  # m1.forward(delay,steps) (0.1,10) 
        time.sleep(2)       # delay between forward and backward
        m1.backward(0.1,10)
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
