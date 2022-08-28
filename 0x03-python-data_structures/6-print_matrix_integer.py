#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    outer_len = len(matrix)
    inner_len = len(matrix[0])
    for i in range(outer_len):
        for j in range(inner_len):
            if j < (inner_len - 1):
                print("{}".format(matrix[i][j]), end=" ")
            else:
                print("{}".format(matrix[i][j]), end="")
        print()
