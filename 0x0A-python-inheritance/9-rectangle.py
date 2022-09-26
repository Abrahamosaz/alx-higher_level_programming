#!/usr/bin/python3
"""
    Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle class representation
    """
    def __init__(self, width, height):
        """
            initialize class instance
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            return the area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
            return the string representation of the rectangle class
        """
        return ("[" + str(self.__class__.__name__) + "] " +
                str(self.__width) + "/" + str(self.__height))
