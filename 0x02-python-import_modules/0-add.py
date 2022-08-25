#!/usr/bin/python3
import add_0 as add_val


def add():
    a = 1
    b = 2
    print("{0:d} + {1:d} = {2:d}".format(a, b, add_val.add(a, b)))


if __name__ == "__main__":
    add()
