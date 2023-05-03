#!/usr/bin/python3
# find the peak of any array

def find_peak(list_of_integers):
    """function to find the peak of integers"""
    arr = list_of_integers
    length = len(arr)
    if length == 0:
        return None
    if length == 1:
        return (arr[0])

    low, high = 0, length - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if (arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]):
            return arr[mid]
        if (arr[mid + 1] > arr[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return (arr[0])
