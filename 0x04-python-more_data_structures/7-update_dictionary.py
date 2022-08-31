#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key_c, value_c in a_dictionary.items():
        if (key_c == key):
            a_dictionary[key_c] = value
    a_dictionary[key] = value
    return (a_dictionary)
