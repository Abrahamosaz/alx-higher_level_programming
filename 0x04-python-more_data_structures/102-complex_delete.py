#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_list = []
    if not value:
        return(a_dictionary)
    for key_c, value_c in a_dictionary.items():
        if (value_c is value):
            del_list.append(key_c)
    for item in del_list:
        del a_dictionary[item]
    return (a_dictionary)
