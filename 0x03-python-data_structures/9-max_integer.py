#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    count = len(my_list) - 1
    idx = 0
    while idx < count:
        if (my_list[idx] > my_list[idx + 1]):
            temp = my_list[idx]
            my_list[idx] = my_list[idx + 1]
            my_list[idx + 1] = temp
        idx += 1
    return (my_list.pop())
