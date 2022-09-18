#!/usr/bin/python3
"""
Module to print a square with a character '#'
Args:
    size (int): size of the square and must be integer otherwise raise error
"""


def print_square(size: int):
    """
    print the size of the square with the '#' character
    """
    if (type(size) is not int or
            (type(size) is float and size < 0)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end='')
        print()
