#!/usr/bin/python

from time import sleep

import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    speeds = [1000, 500, 250, 150, 100, 50]

    currentSpeedIndex = 0
    msPassed = 0
    ledOn = False
    cycleMs = 50

    while True:
        if msPassed >= speeds[currentSpeedIndex]:
            ledOn = ~ledOn
            msPassed = 0
            GPIO.output(4, ledOn)
        buttonPressed = GPIO.input(14) == 0
        if buttonPressed == True:
            print 'Button pressed'
            currentSpeedIndex = (currentSpeedIndex + 1) % len(speeds)
            print 'New speed: ' + str(speeds[currentSpeedIndex]) + 'ms'
        sleep(cycleMs / 1000.0)
        msPassed += cycleMs
except KeyboardInterrupt:
    GPIO.output(4, False)
finally:
    GPIO.cleanup()
