#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus
import time

bus = smbus.SMBus(1)
address = 0x49

def getTemp():
    bus.read_byte_data(address, 0xEE)
    tempFull = bus.read_byte_data(address, 0xAA)
    counter = bus.read_word_data(address, 0xA8)
    slope = bus.read_word_data(address, 0xA9)
    temp = tempFull - 0.25 + float(slope - counter) / slope
    bus.read_byte_data(address, 0x22)
    return temp

while True:
    for c in '%9.1f' % round(getTemp(), 1) + ' C':
        bus.write_byte(0x23, ord(c))    
    time.sleep(1)
