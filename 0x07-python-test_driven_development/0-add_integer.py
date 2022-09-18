#!/usr/bin/python3
"""
Module to add two integers together
Args:  must be an integer otherwise must be converted if posible
Return: return te result of first and second argument
"""


def add_integer(a, b=98) -> int:
    """second argument have a default value of 98
    return integer value (sum of a + b)
    """
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
