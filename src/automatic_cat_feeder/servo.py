import time
import datetime


import board 
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
import adafruit_motor 
import adafruit_pca9685

import read_stream

#i2c = busio.I2C(board.SCL, board.SDA)
#pca = adafruit_pca9685PCA9685(i2c)
#pca.frequency = 50
#servo_persephone = adafruit_motor.servo.Servo(pca.channels[7])
#servo_eris = adafruit_motor.servo.Servo(pca.channels[5])


def setup_servo():
    for i in range(0):
        #servo_persephone.angle = i
        #servo_eris.angle = i
        time.sleep(0.5)
      
   
def open_bowl(cat):
    if cat == "persephone":
        #open_persephone()
        #close_eris()
        time.sleep(0.5)

    if cat == "eris":
        #open_eris()
        #close_persephone()
        time.sleep(0.5)


    if cat == "other":
        #close_persephone()
        #close_eris()
        time.sleep(0.5)

                       

def open_persephone():
    for i in range(180):
        #servo_persephone.angle = i
        time.sleep(0.03)
   


def open_eris():
    for i in range(180):
        #servo_eris.angle = i
        time.sleep(0.03)


def close_persephone():
    for i in range(180):
        #servo_persephone.angle = 180 - i
        time.sleep(0.03)
            
   

def close_eris():
    for i in range(180):
        #servo_eris.angle = 180 - i
        time.sleep(0.03)
