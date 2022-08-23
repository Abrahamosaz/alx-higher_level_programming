#!/usr/bin/python3
for i in range(9):
    for j in range(8):
        if (i == j and j == i):
            continue
        else:
            print("{:d}{:d}".format(i, j), end="")
        if (i < 8 and j < 9):
            print(", ", end="")
print()
