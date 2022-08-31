#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    check_list = list(a_dictionary.values())
    length = len(check_list) - 1
    idx = 0
    while length > 0:
        if (check_list[idx] > check_list[idx + 1]):
            temp = check_list[idx]
            check_list[idx] = check_list[idx + 1]
            check_list[idx + 1] = temp
        idx += 1
        length -= 1
    for key, value in a_dictionary.items():
        if value == check_list[-1]:
            return (key)
