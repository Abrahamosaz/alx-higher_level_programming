#!/usr/bin/python3
def uniq_add(my_list=[]):
    total_value = 0
    for i in set(my_list):
        total_value += i
    return total_value
