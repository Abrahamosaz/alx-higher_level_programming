#!/usr/bin/python3

"""Define a class square"""


class Square:
    """creating a new class Square"""

    def __init__(self, size=0):
        """Initilize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """return the size of the sqaure instance"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """set the siz property of instances"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of square instance"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the sqaure in '#' for all instances of the class"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            [print('#', end='') for j in range(self.__size)]
            print()
