#!/usr/bin/python3
"""
    function that write to a file
"""


def write_file(filename="", text=""):
    """
        write text to file
    """
    no_of_chars = 0
    with open(file=filename, mode="w", encoding="utf-8") as file:
        no_of_chars = file.write(text)
    return (no_of_chars)
