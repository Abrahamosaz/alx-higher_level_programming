#!/usr/bin/python3

"""Define a class square"""


class Square:
    """creating a class square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the atrribute of a class instance
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """return the size of the class instance"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter function for setting the attribute of the cass instancee"""
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """return the position of the class instance"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter function for setting the attribute of the class instance"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of two \
                    positive integers")
        self.__position = value

    def area(self):
        """return  the area of the class instance"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with '#' and
        don't file line whn position[1] > 0
        """
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end="") for j in range(0, self.__position[0])]
            [print('#', end='') for k in range(0, self.__size)]
            print()
