#!/usr/bin/python3
""""
    class student
"""


class Student:
    """
        student class
    """
    def __init__(self, first_name, last_name, age):
        """
            inittialize student instances
            Args:
                first_name (str): firstname of the student
                last_name (str): lastname of the student
                age (int); age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            return the dictionary representation of the class
        """
        return (Student(self.first_name, self.last_name,
                self.age).__dict__)
