#!/usr/bin/python3
"""
    square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        class square
    """
    def __init__(self, size):
        """
            initialize instance of the sqaure class
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            return the area of the square
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
            return the representation of square class
        """
        return ("[" + str(Rectangle.__name__) + "] " +
                str(self.__size) + "/" + str(self.__size))
