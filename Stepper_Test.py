import RPi.GPIO as GPIO                        #Import GPIO library
import PiMotor
import time

m1 = PiMotor.Stepper("STEPPER1")

# Rotate Stepper 1 Contiously in forward/backward direction

try:
    while True:
        m1.forward(0.1,10)  # Delay and rotations
        time.sleep(2)
        m1.backward(0.1,10)
        time.sleep(2)


except KeyboardInterrupt:
    GPIO.cleanup()