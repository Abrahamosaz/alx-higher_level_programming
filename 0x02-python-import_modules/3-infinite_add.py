#!/usr/bin/python3
import sys

count = 0
for i in range(len(sys.argv)):
    count += 1
sum_val = 0
idx = 1
while count != 1:
    sum_val += int(sys.argv[idx])
    idx += 1
    count -= 1
if __name__ == "__main__":
    print(sum_val)
