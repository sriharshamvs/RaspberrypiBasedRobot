import RPi.GPIO as GPIO
from time import sleep

## Setup the Hardware
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_1 = 2
LED_2 = 3
GPIO.setup(LED_1,GPIO.OUT)
GPIO.output(LED_1,0)
GPIO.setup(LED_2,GPIO.OUT)
GPIO.output(LED_2,0)


def responseToTheRequest(data):
    response=b''
    if data == 0:
        GPIO.output(LED_1,0)
        GPIO.output(LED_2,0)
        response = b'RED OFF & GREEN OFF'
    elif data == 1:
        GPIO.output(LED_1,1)
        GPIO.output(LED_2,0)
        response = b'RED ON & GREEN OFF'
    elif data == 2:
        GPIO.output(LED_1,0)
        GPIO.output(LED_2,1)
        response = b'RED OFF & GREEN ON'
    elif data == 3:
        GPIO.output(LED_1,1)
        GPIO.output(LED_2,1)
        response = b'RED ON & GREEN ON'
    else :
        GPIO.output(LED_1,0)
        GPIO.output(LED_2,0)
        print("Invalid")
        response = b'-1'
    return response
