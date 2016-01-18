#!/usr/bin/python

from time import sleep

import RPi.GPIO as GPIO

pin = 14

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    while True:
        GPIO.output(pin, 1)
        sleep(1)
        GPIO.output(pin, 0)
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
