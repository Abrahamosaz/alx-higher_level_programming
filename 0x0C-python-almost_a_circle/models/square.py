#!/usr/bin/python3
"""
    class sqaure
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        square class inherit from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initailze class instances
            Args:
                size (int): size of the sqaure
                x (int): x coordinate of the square
                y (int); y coordinate of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            return the string representation of the square class
        """
        return ("[" + str(self.__class__.__name__) + "] " + "(" +
                str(self.id) + ") " + str(self.x) + "/" + str(self.y) +
                " - " + str(self.width))

    @property
    def size(self):
        """
            return the size of the square
        """
        return (self.width)

    @size.setter
    def size(self, value):
        if self.integer_validator("width", value):
            self.width = value

    def update(self, *args, **kwargs):
        if args:
            for idx, value in enumerate(args, start=1):
                if idx == 1:
                    self.id = value
                elif idx == 2:
                    self.size = value
                elif idx == 3:
                    self.x = value
                else:
                    self.y = value
        elif not args and kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        __dict__ = {}
        __dict__["id"] = self.id
        __dict__["size"] = self.id
        __dict__["x"] = self.x
        __dict__["y"] = self.y
        return (__dict__)
