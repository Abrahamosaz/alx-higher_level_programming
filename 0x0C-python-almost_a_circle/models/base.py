#!/usr/bin/python3
"""
    Base class
"""
import json


class Base:
    """
        Base class
        Args:
            _nb_objects (int): class attribute of
            id instances value
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            initialize Base class instances
            Args:
                id (int): id of clas instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return (json_string)

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string is None:
            return []
        string = json.loads(json_string)
        return (string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            save json string to a file
        """
        try:
            new_list_objs = list(map(lambda x: x.to_dictionary(), list_objs))
            json_string = cls.to_json_string(new_list_objs)
        except Exception:
            pass
        filename = str(cls.__name__) + ".json"
        with open(file=filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("")
            else:
                file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            create new isnstances with dictionary attriute
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
            load json string from a file
        """
        filename = str(cls.__name__) + ".json"
        with open(file=filename, mode="r", encoding="utf-8") as file:
            json_string = file.read()
        python_list = cls.from_json_string(json_string)
        new_instances = []
        for inst in python_list:
            new_instances.append(cls.create(**inst))
        return (new_instances)
