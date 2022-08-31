#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    my_list = []
    for key_c, value_c in a_dictionary.items():
        if (key_c == key):
            my_list.append(key_c)
    if not len(my_list):
        return (a_dictionary)
    for i in range(len(my_list)):
        del a_dictionary[my_list[i]]
    return (a_dictionary)
