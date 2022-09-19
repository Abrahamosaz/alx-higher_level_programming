#!/usr/bin/python3
"""
Module to that contain afunction that print first and last name
Args: arguments must be string of first name and last name
last name is empty by default
"""


def say_my_name(first_name, last_name=""):
    """"
    first and last name must be a string otherwise it raise error
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    elif (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {0:s} {1:s}".format(first_name, last_name))
