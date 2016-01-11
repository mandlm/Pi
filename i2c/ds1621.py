#!/usr/bin/env python

import smbus

bus = smbus.SMBus(1)
address = 0x49

print 'Start: ' + hex(bus.read_byte_data(address, 0xEE))

tempFull = bus.read_byte_data(address, 0xAA)
print 'Temp (1 deg): ' + str(tempFull)

halfDegreeTemp = bus.read_word_data(address, 0xAA)
tempHalf = halfDegreeTemp & 0x00FF
if halfDegreeTemp & 0xFF00:
    tempHalf += 0.5
print 'Temp (0.5 deg): ' + str(tempHalf)

counter = bus.read_word_data(address, 0xA8)
print 'Counter: ' + str(counter)

slope = bus.read_word_data(address, 0xA9)
print 'Slope: ' + str(slope)

tempHi = tempFull - 0.25 + float(slope - counter) / slope
print 'Temp (hi-res): ' + str(tempHi)

print 'End: ' + hex(bus.read_byte_data(address, 0x22))



