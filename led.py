#!/usr/bin/python

from time import sleep

import RPi.GPIO as GPIO

print 'blah'

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)

    while True:
        GPIO.output(4, 1)
        sleep(1)
        GPIO.output(4, 0)
        sleep(1)
except KeyboardInterrupt:
    GPIO.output(4, 0)
finally:
    GPIO.cleanup()

print 'end'
