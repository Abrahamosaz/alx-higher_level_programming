#!/usr/bin/python3
"""
    check if an object is exactly and instance of a particular class
"""


def is_same_class(obj, a_class):
    """
        check if obj is an instance of a_class
    """
    if (type(obj) is a_class):
        return True
    return False
