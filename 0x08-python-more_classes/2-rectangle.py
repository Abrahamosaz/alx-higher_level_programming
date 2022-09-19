#!/usr/bin/python3
"""
    Rectangle class
"""


class Rectangle:
    """
        __init__ method: initialize the class instances
        Args:
            width (int): width of the rectangle
            height (int): height of thr rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            return the width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            return the height of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            return the area of the rectangle
        """
        return (self.__width * self.height)

    def perimeter(self):
        if (not self.__width or not self.__height):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
