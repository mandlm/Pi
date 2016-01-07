#!/usr/bin/python

from time import sleep

import RPi.GPIO as GPIO

yellowLed = 15
redLed = 17
greenLed = 18

buttonPin = 27

sleepTime = 0.25

def buttonHandler(channel):
    print 'button pushed'

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(yellowLed, GPIO.OUT)
    GPIO.setup(redLed, GPIO.OUT)
    GPIO.setup(greenLed, GPIO.OUT)

    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=buttonHandler, bouncetime=1000)    

    while True:
        GPIO.output(yellowLed, 1)
        GPIO.output(redLed, 0)
        GPIO.output(greenLed, 0)
        sleep(sleepTime)
        GPIO.output(yellowLed, 0)
        GPIO.output(redLed, 1)
        GPIO.output(greenLed, 0)
        sleep(sleepTime)
        GPIO.output(yellowLed, 0)
        GPIO.output(redLed, 0)
        GPIO.output(greenLed, 1)
        sleep(sleepTime)
except KeyboardInterrupt:
    GPIO.output(yellowLed, 0)
    GPIO.output(redLed, 0)
    GPIO.output(greenLed, 0)
finally:
    GPIO.cleanup()
