#!/usr/bin/python3
import sys
length = len(sys.argv)
if (length == 1):
    print("{0:d} arguments.".format(length - 1))
elif (length > 1):
    if (length - 1 == 1):
        print("{0:d} argument:".format(length - 1))
    elif (length > 1):
        print("{0:d} arguments:".format(length - 1))
    for i in range(length - 1):
        print("{0:d}: {1:s}".format(i + 1, sys.argv[i + 1]))
