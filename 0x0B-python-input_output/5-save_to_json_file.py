#!/usr/bin/python3
"""
    function that save to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
        save object to .json file
    """
    with open(file=filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
