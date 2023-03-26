import PiMotor
import time
import RPi.GPIO as GPIO

# This is for Longruner 5X Geared Stepper Motor
# 28byj 48 Uln2003 5v Stepper Motor Uln2003 Driver Board
# This url contains how to connect your motors right and much more: 
#	http://www.4tronix.co.uk/arduino/Stepper-Motors.php

m1 = PiMotor.Stepper("STEPPER1")
m1.setSequence([
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
        [1,0,0,1]
   ])

# Rotate Stepper 1 Contiously in forward/backward direction
# Rotating the fastest the motor can go
while True:
    try:
        m1.forward(0.001,512)  # Delay and steps
        time.sleep(2)
        m1.backward(0.001,512)
        time.sleep(2)
    except KeyboardInterrupt:
        GPIO.cleanup()
