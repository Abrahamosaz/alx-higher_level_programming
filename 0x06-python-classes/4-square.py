#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represent a square """

    def __init__(self, size=0):
        """Initilaize  a square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """return the value of the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set the size attribute of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)
