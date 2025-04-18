import RPi.GPIO as GPIO
import time
import threading
import PiMotor

# ----------- PiMotor Arrow Setup -----------
a1 = PiMotor.Arrow(1)
a2 = PiMotor.Arrow(2)
a3 = PiMotor.Arrow(3)
a4 = PiMotor.Arrow(4)
arrow_sequence = [a1, a2, a3, a4]

# ----------- Servo Setup -----------
SERVO1_PIN = 12  # Physical pin 12 (GPIO18)
SERVO2_PIN = 7   # Physical pin 7 (GPIO4)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO1_PIN, GPIO.OUT)
GPIO.setup(SERVO2_PIN, GPIO.OUT)

pwm1 = GPIO.PWM(SERVO1_PIN, 50)
pwm2 = GPIO.PWM(SERVO2_PIN, 50)

pwm1.start(0)
pwm2.start(0)

def set_angle(pwm, angle):
    """Rotate servo to given angle."""
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.02)

def arrow_rotation():
    """Rotate the arrows continuously in sequence."""
    while True:
        for arrow in arrow_sequence:
            arrow.on()
            time.sleep(0.1)
            arrow.off()

def servo_sweep(pwm, name="Servo"):
    """Continuously sweep servo back and forth."""
    try:
        while True:
            for angle in range(0, 181, 5):
                set_angle(pwm, angle)
            for angle in range(180, -1, -5):
                set_angle(pwm, angle)
    except:
        print(f"{name} Stopped")

# ----------- Threading Setup -----------
try:
    print("Starting demo: arrows rotating, servos sweeping.")

    # Start rotating arrows in a background thread
    arrow_thread = threading.Thread(target=arrow_rotation, daemon=True)
    arrow_thread.start()

    # Start both servos in their own threads
    servo1_thread = threading.Thread(target=servo_sweep, args=(pwm1, "Servo1"), daemon=True)
    servo2_thread = threading.Thread(target=servo_sweep, args=(pwm2, "Servo2"), daemon=True)
    servo1_thread.start()
    servo2_thread.start()

    while True:
        time.sleep(1)  # Keep main thread alive

except KeyboardInterrupt:
    print("Demo interrupted")

finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
    print("Cleaned up GPIO")
