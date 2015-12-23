#!/usr/bin/python

from time import sleep

import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    last_state = True
    last_led_state = False

    while True:
        input_state = GPIO.input(14)
        if input_state == False and input_state != last_state:
            print 'Button pressed'
            GPIO.output(4, ~last_led_state)
            last_led_state = ~last_led_state
        last_state = input_state
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.output(4, False)
finally:
    GPIO.cleanup()
