#!/usr/bin/env python

import sys
import smbus

bus = smbus.SMBus(1)
address = 0x23

for c in sys.argv[1]:
    bus.write_byte(address, ord(c))
    
