#!/usr/bin/python3
for i in range(ord("a"), ord("z") + 1):
    if (chr(i) != 'q' and chr(i) != 'e'):
        print("{0:s}".format(chr(i)), end="")
