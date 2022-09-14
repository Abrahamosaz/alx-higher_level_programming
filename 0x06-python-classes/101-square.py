#!/usr/bin/python3


class Square:
    """representing a type for sqaure"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise a class instances
        Args:
            size (int): The size of the sqaure
            position (tuple): The position specified
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrive the value of the atrribute size form this getter method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrive the position to set the value"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all((num >= 0 for num in value))):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """calculate the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the sqaure to thhe stdout with '#'
            and with the position given
        """
        if self.__size == 0:
            print()
            return
        [print() for line in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for j in range(0, self.__position[0])]
            [print('#', end='') for k in range(0, self.__size)]
            print()

    def __str__(self):
        """string representation of class instances"""
        if self.__size == 0:
            print()
            return ("")
        [print() for line in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for j in range(0, self.__position[0])]
            [print('#', end='') for k in range(0, self.__size)]
            if i != self.__size - 1:
                print()
        return("")
