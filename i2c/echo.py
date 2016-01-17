#!/usr/bin/env python

import smbus

bus = smbus.SMBus(1)
address = 0x23

def send(data):
    print 'Send / receive: ' + str(data) + ' / ' + str(bus.read_byte_data(address, data))


for d in range(1, 5):
    send(d)
