#!/usr/bin/python3
for x in range(-122, -96):
    if x % 2 == 0:
        x = (x * -1)
    else:
        x = (x * -1) - 32
    print("{}".format(chr(x)), end='')
