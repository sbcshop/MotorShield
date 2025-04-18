import RPi.GPIO as GPIO
import time

# Define physical pins for servos
SERVO1_PIN = 12  # Physical pin 12 (GPIO18)
SERVO2_PIN = 7   # Physical pin 7 (GPIO4)

# Set up GPIO mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO1_PIN, GPIO.OUT)
GPIO.setup(SERVO2_PIN, GPIO.OUT)

# Set up 50Hz PWM for both servos
pwm1 = GPIO.PWM(SERVO1_PIN, 50)
pwm2 = GPIO.PWM(SERVO2_PIN, 50)

pwm1.start(0)
pwm2.start(0)

def set_angle(pwm, angle):
    """
    Rotate a servo to a specified angle using the given PWM object.
    """
    duty_cycle = (angle / 18) + 2  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Move both servos together
        set_angle(pwm1, 0)
        set_angle(pwm2, 0)
        time.sleep(1)

        set_angle(pwm1, 90)
        set_angle(pwm2, 90)
        time.sleep(1)

        set_angle(pwm1, 180)
        set_angle(pwm2, 180)
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
