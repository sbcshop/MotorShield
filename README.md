# Motor-Shield

Motor Driver for Raspberry Pi to control DC and Stepper Motors

<img src="https://cdn.shopify.com/s/files/1/1217/2104/products/motor_shield_a_720_660_1024x1024.png?v=1528533987" width="300">

**Steps for Motor Shield software installation -** 

1. Open Terminal and download the code by writing: 
   ```
   git clone https://github.com/sbcshop/MotorShield.git
   ```

2. Your code will be downloaded to '/home/pi' directory. Use 'ls' command to check the list of directories.

3.  Go to directory 'MotorShield' and open 'Test_Motor.py'

4. Run (Press F5) file 'Test_Motor.py'. This is the example code to run all the motors in 'Forward' and 'Backward' direction

5. For interfacing Stepper Motor use example code 'Stepper_Test.py'



## PiRlay GUI
![PiRelay GUI](https://github.com/sbcshop/MotorShield/blob/master/Images/PiRelay_GUI.png)

**Changes:**

Added __Motor__, __LinkedMotor__, __Arrow__ and __Sensor__ classes. Allows user to specify what is "forward" and what is "reverse" without requiring re-wiring of the motors.
