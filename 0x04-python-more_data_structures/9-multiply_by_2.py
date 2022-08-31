#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_list = []
    for key, value in a_dictionary.items():
        my_list.append([key, value * 2])
    return (dict(my_list))
