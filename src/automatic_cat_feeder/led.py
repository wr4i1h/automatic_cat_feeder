import RPi.GPIO as GPIO
import time


def setup_led():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)


def error_led():
    GPIO.output(21,GPIO.HIGH)
    GPIO.output(20,GPIO.LOW)




def ok_led():
    GPIO.output(20,GPIO.HIGH)    
    GPIO.output(21,GPIO.LOW)

