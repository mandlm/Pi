#!/usr/bin/python

from time import sleep

import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    last_state = True

    while True:
        input_state = GPIO.input(14)
        if input_state == False and input_state != last_state:
            print 'Button pressed'
        last_state = input_state
        sleep(0.2)
finally:
    GPIO.cleanup()
