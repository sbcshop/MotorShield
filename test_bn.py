import PiMotor
import adafruit_bno055
import board

i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

print(sensor.temperature)
print(sensor.euler)
print(sensor.gravity)

