#!/usr/bin/python3
"""
Module containa function that print text with 2 new line
after each of thes character '.', ':', and '?'
Args: is as string of text words otherwise raise error
"""


def text_indentation(text: str):
    """"
    function that print text with two new line base on some charcters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    idx = 0
    while (idx < len(text)):
        if (text[idx] == '.' or text[idx] == '?' or
                text[idx] == ':'):
            print(text[idx], end='')
            try:
                if (text[idx + 1] == ' '):
                    idx += 1
            except IndexError:
                break
            print("\n")
        else:
            print(text[idx], end='')
        idx += 1
