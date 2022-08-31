#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    div_value = 0
    sum_value = 0
    for tuple_av in my_list:
        div_value += tuple_av[1]
        sum_value += (tuple_av[0] * tuple_av[1])
    return (sum_value / div_value)
