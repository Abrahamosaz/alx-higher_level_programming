#!/usr/bin/python3
"""
    read a file with filename and print to stdout file stream
"""


def read_file(filename=""):
    """
        print contents of a file read to the stdout
    """
    with open(file=filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
