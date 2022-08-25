#!/usr/bin/python3
def simple_cal(argv, exit, cal):
    count = len(argv)
    if (count < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
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
            exit(1)


if __name__ == "__main__":
    import sys
    import calculator_1 as cal
    simple_cal(sys.argv, sys.exit, cal)
