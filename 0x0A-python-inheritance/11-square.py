#!/usr/bin/python3
"""
    Square class inherit from Rectangle  class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        square class
    """
    def __init__(self, size):
        """
            initialize the square instance class
            Args:
                size (int); size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            return the area of the square
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
            return the string representation of the square
        """
        return ("[" + str(self.__class__.__name__) + "] " +
                str(self.__size) + "/" + str(self.__size))
