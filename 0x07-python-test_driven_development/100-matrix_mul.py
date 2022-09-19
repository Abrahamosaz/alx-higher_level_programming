#!/usr/bin/python3
"""
    matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """
        matrix multiplication
    """
    if (type(m_a) is not list):
        raise TypeError("m_a must be a list")
    elif (type(m_b) is not list):
        raise TypeError("m_b must be a list")
    elif (not all([isinstance(item_list, list) for item_list in m_a])):
        raise TypeError("m_a must be a list of lists")
    elif (not all([isinstance(item_list, list) for item_list in m_b])):
        raise TypeError("m_a must be a list of lists")
    elif (not len(m_a) or not all([len(item_list) > 0 for item_list in m_a])):
        raise ValueError("m_a can't be empty")
    elif (not len(m_b) or not all([len(item_list) > 0 for item_list in m_b])):
        raise ValueError("m_b can't be empty")
    elif not all((isinstance(el, float) or isinstance(el, int))
            for el in [x for item in m_a for x in item]):
        raise TypeError("m_a should contain only integers or floats")
    elif not all((isinstance(el, int) or isinstance(el, float))
            for el in [x for item in m_b for x in item]):
        raise TypeError("m_b should contain only integers or floats")
    if not all([len(row) == len(m_a[0]) for row in m_a]):
        raise TypeError("each row of m_a must be of the same size")
    if not all([len(row) == len(m_b) for row in m_b]):
        raise TypeError("each row of m_b must be of the same size")
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    transpose_list = []
    for col in range(len(m_b[0])):
        inner_list = []
        for row in range(len(m_b)):
            inner_list.append(m_b[row][col])
        transpose_list.append(inner_list)

    new_list = []
    for row in m_a:
        inner_list = []
        for col in transpose_list:
            value = 0
            for i in range(len(transpose_list[0])):
                value += row[i] * col[i]
            inner_list.append(value)
        new_list.append(inner_list)
    return (new_list)
