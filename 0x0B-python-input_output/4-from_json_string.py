#!/usr/bin/python3
"""
    function return python string from json string
"""
import json


def from_json_string(my_str):
    """
        return the python string reopresentation of json string `my_str`
    """
    return (json.loads(my_str))
