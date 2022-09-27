#!/usr/bin/python3
"""
    function that create object from json file
"""
import json


def load_from_json_file(filename):
    """
        create object from .json file
    """
    with open(file=filename, mode="r", encoding="utf-8") as file:
        my_string = json.load(file)
    return (my_string)
