#!/usr/bin/python3
"""
Module contain a function divide all the element of the matrix
Args: the function takes a list as first argument and a
    scaler number as second that will divide the matrix
"""


def matrix_divided(matrix: list, div: int) -> list:
    """"
    matrix is a list of lists of integers and float
    """
    new_list = []
    if (not isinstance(matrix, list) or
            not all([isinstance(items, list) for items in matrix])):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    elif (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    for lists in matrix:
        if (len(lists) is not len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        for value in lists:
            if (type(value) is not int
                    and type(value) is not float):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            inner_list.append(round((value / div), 2))
        new_list.append(inner_list)
    return (new_list)
