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

    def to_json(self, attrs=None):
        """
            return the dictionary representation of the class
        """
        student_dict =\
            Student(self.first_name, self.last_name, self.age).__dict__
        if (attrs is not None and
                all([isinstance(word, str) for word in attrs])):
            new_dict = {}
            for item in student_dict.keys():
                if item in attrs:
                    new_dict[item] = student_dict[item]
            return (new_dict)
        return (student_dict)

    def reload_from_json(self, json):
        """
            reinstialize class attribute
            Args;
                json (dict): dictionary for reinstailizing
        """
        for item in json:
            if item in self.to_json():
                setattr(self, item, json[item])
