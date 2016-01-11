#!/usr/bin/env python

import smbus

bus = smbus.SMBus(1)

for address in range(0, 127):
    try:
        bus.read_byte(address)
        print 'device at address ' + hex(address)
    except IOError:
        pass
    
