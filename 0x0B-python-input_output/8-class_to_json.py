#!/usr/bin/python3
"""
    function return a dictionary description of data type
"""


def class_to_json(obj):
    """
        return a dictionary description of the class object
    """
    return (obj.__dict__)
