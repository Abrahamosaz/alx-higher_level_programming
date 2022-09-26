#!/usr/bin/python3
"""
    return a list of available atrributye and method
"""


def lookup(obj):
    """
        return a list of attribute and method from the obj parameter
    """
    return (dir(obj))
