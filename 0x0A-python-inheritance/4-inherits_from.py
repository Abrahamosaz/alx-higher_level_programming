#!/usr/bin/python3
"""
    check if object is a sub class not a class of a
    specified class given
"""


def inherits_from(obj, a_class):
    """
        return True is obj is a sub class of a_class and
        False if it's a class of a_class
    """
    if(issubclass(obj.__class__, a_class) and not type(obj) == a_class):
        return True
    return False
