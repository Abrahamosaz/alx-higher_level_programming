#!/usr/bin/python3
"""
    function that append to the end of the file
"""


def append_write(filename="", text=""):
    """
        append text to the file
    """
    no_chars = 0
    with open(file=filename, mode="a", encoding="utf-8") as file:
        no_chars = file.write(text)
    return (no_chars)
