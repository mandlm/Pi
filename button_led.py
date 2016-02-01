#!/usr/bin/python

from time import sleep

import RPi.GPIO as GPIO

ledPin = 14
buttonPin = 16

def buttonHandler(channel):
    GPIO.output(ledPin, not GPIO.input(ledPin))

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=buttonHandler, bouncetime=300)

    GPIO.output(ledPin, False)
    
    while True:
        GPIO.wait_for_edge(15, GPIO.RISING)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
