#!/usr/bin/python3
def discovr(hidden_4):
    name = dir(hidden_4)
    for i in name:
        if i[:2] != '--':
            print("{:s}".format(i))


if __name__ == "__main__":
    import hidden_4
    discovr(hidden_4)
