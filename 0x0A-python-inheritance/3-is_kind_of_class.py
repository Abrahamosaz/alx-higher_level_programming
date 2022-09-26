#!/usr/bin/python3
"""
    check if an object is a instance of a specific class or a subclass
"""


def is_kind_of_class(obj, a_class):
    """
        check if object is an instance of a_class ior a sub class
    """
    if (issubclass(obj.__class__, a_class)):
        return True
    return False
