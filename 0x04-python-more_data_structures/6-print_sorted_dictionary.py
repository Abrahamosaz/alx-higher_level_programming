#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary)
    for i in range(len(sort_keys)):
        print("{0}: {1}".format(sort_keys[i], a_dictionary.get(sort_keys[i])))
