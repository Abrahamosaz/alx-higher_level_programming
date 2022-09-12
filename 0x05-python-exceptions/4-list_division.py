#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    index = 0
    while True:
        if index < list_length:
            try:
                result = my_list_1[index] / my_list_2[index]
            except ZeroDivisionError:
                print("division by zero")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            except TypeError:
                print("wrong type")
                result = 0
            finally:
                new_list.append(result)
                index += 1
        else:
            return (new_list)
