#!/usr/bin/python

import ConfigParser
import RPi.GPIO as GPIO

yellowLed = 15
redLed = 17
greenLed = 18

def setLeds(yellow, red, green):
    GPIO.output(yellowLed, yellow)
    GPIO.output(redLed, red)
    GPIO.output(greenLed, green)

config = ConfigParser.ConfigParser()
config.read('/etc/mopidy/mopidy.conf')

ledColor = config.get('moped-switcher', 'led')

GPIO.setmode(GPIO.BCM)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)

if ledColor == 'yellow':
    print 'yellow'
    setLeds(1, 0, 0)
elif ledColor == 'red':
    setLeds(0, 1, 0)
elif ledColor == 'green':
    setLeds(0, 0, 1)

GPIO.cleanup()
