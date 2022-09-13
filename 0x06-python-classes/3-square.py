#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represent a sqaure"""

    def __init__(self, size=0):
        """initialise an instance of the sqaure class
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """find the area of instance of a square"""
        return (self.__size * self.__size)
