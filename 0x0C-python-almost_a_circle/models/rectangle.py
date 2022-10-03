#!/usr/bin/python3
"""
    class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle
    """
    @staticmethod
    def integer_validator(name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{:s} must be > 0".format(name))
        elif name == "x" or name == "y":
            if value < 0:
                raise ValueError("{:s} must be >= 0".format(name))
        return True

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initailize the ractangle class instances
            Args:
                width (int): width of the Rectangle
                height (int): height of the rectangle
                x (int): x coordinate of the rectangle
                y (int): y coordinate of the rectangle
        """
        if id is None or self.integer_validator("id", id):
            super().__init__(id)
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
        if self.integer_validator("x", x):
            self.__x = x
        if self.integer_validator("y", y):
            self.__y = y

    @property
    def width(self):
        """
            return the width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if self.integer_validator("width", value):
            self.__width = value

    @property
    def height(self):
        """
            return the height of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if self.integer_validator("height", value):
            self.__height = value

    @property
    def x(self):
        """
            return the x coordinate of the
            rectangle
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        if self.integer_validator("x", value):
            self.__x = value

    @property
    def y(self):
        """
            return the y coordinate of the
            rectangle
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        if self.integer_validator("y", value):
            self.__y = value

    def area(self):
        """
            return the area of the rectangle
        """
        return (self.width * self.height)

    def display(self):
        """
            dsiplay the rectangle shape with '#'
        """
        [print() for x in range(self.y)]
        for i in range(self.height):
            [print(' ', end="") for y in range(self.x)]
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
            return the string representation of the rectangle
        """
        return ("[" + str(self.__class__.__name__) + "] " + "(" +
                str(self.id) + ") " + str(self.x) + "/" +
                str(self.y) + " - " + str(self.width) +
                "/" + str(self.height))

    def update(self, *args, **kwargs):
        """
            update the class attribute with args and kwargs
        """
        if len(args):
            for index, value in enumerate(args, start=1):
                if index == 1:
                    self.id = value
                elif index == 2:
                    self.width = value
                elif index == 3:
                    self.height = value
                elif index == 4:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
            return dictionary of class atrribute
        """
        __dict__ = {}
        __dict__["id"] = self.id
        __dict__["width"] = self.width
        __dict__["height"] = self.height
        __dict__["x"] = self.x
        __dict__["y"] = self.y
        return (__dict__)
