#!/usr/bin/python

import glob
import os
import subprocess

import RPi.GPIO as GPIO

mopidyConf = '/etc/mopidy/mopidy.conf'
userDir = '/etc/mopidy/conf.user/'

def stopMopidy():
    command = ['service', 'mopidy', 'stop']
    subprocess.call(command, shell=False)

def startMopidy():
    command = ['service', 'mopidy', 'start']
    subprocess.call(command, shell=False)

def getConfigs():
    return sorted(glob.glob(os.path.join(userDir, '*.conf')))

def getCurrentConfig():
    if os.path.islink(mopidyConf):
        return os.path.realpath(mopidyConf)
    else:
        return None

def getNextConfig():
    currentConfig = getCurrentConfig()
    availableConfigs = getConfigs()    
    currentIndex = availableConfigs.index(currentConfig)
    nextIndex = (currentIndex + 1) % len(availableConfigs)
    return availableConfigs[nextIndex]

def setConfig(newConfig):
    if os.path.islink(mopidyConf) and os.path.isfile(newConfig):
        os.unlink(mopidyConf)
        os.symlink(newConfig, mopidyConf)

def switchConfig():
    setConfig(getNextConfig())
    
def buttonHandler(channel):
    print 'Switching to ' + getNextConfig()
    try:
        stopMopidy()
        switchConfig()
        startMopidy()
    except OSError as e:
        print 'Error: ' + e.strerror
    
if __name__ == '__main__':
    buttonPin = 4
    dummyPin = 15
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(dummyPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=buttonHandler, bouncetime=1000)

    try:
        while True:
            GPIO.wait_for_edge(dummyPin, GPIO.RISING)
    finally:
        GPIO.cleanup()
