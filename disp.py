#!/usr/bin/env python3

import fileinput

for line in fileinput.input():
    if line.startswith("Notification handle = 0x0024 value:"):
        print(end="   ")
        vals = line.split()[5:]
        # XORing the first (static) and third (random) bytes
        # with the data give us simple BCD °C
        x = int(vals[0], 16) ^ int(vals[2], 16)
        for i in [6, 7, 8]:
            print(int(vals[i+1], 16) ^ x, end='')
        print(end="°C   ")
        for i in [13, 14, 15]:
            print(int(vals[i+1], 16) ^ x, end='')
        print("°C")
    else:
        print(line, end='')

