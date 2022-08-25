#!/usr/bin/python3
import sys
import calculator_1 as cal


def simple_cal():
    count = len(sys.argv)
    if (count < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if (operator == '+'):
            print("{0:d} + {1:d} = {2:d}".format(a, b, cal.add(a, b)))
        elif (operator == '-'):
            print("{0:d} - {1:d} = {2:d}".format(a, b, cal.sub(a, b)))
        elif (operator == '*'):
            print("{0:d} * {1:d} = {2:d}".format(a, b, cal.mul(a, b)))
        elif (operator == '/'):
            print("{0:d} / {1:d} = {2:d}".format(a, b, cal.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)


if __name__ == "__main__":
    simple_cal()
