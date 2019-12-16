import PiMotor
import time

a1 = PiMotor.Arrow(1)
a2 = PiMotor.Arrow(2)
a3 = PiMotor.Arrow(3)
a4 = PiMotor.Arrow(4)

try:
    while True:
        print("All LEDs On.")
        a1.on()
        a2.on()
        a3.on()
        a4.on()
        time.sleep(5)
        print("All LEDs Off.")
        a1.off()
        a2.off()
        a3.off()
        a4.off()
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()