#!/usr/bin/python3
"""
    BaseGeometry class
"""


class BaseGeometry(object):
    """
        BaseGeometry class
    """
    def area(self):
        """
            return the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validate integer value
        """
        if (type(value) is not int):
            raise TypeError("{} must be integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))