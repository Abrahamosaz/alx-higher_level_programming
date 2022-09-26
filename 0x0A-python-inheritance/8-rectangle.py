#!/usr/bin/python3
"""
    Rectangle class that inherit from base class BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle class
    """
    def __init__(self, width, height):
        """
            initialize the class
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
