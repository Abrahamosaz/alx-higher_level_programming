#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    tb = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    prev, _sum = 0, 0
    for ch in roman_string:
        _sum += tb[ch] if tb[ch] <= prev else tb[ch] - prev * 2
        prev = tb[ch]
    return (_sum)
