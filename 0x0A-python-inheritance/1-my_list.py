#!/usr/bin/python3
"""
   function that inherits from list type
"""


class MyList(list):
    """
        function the inherit from list class wit additional
        method
    """
    def print_sorted(self):
        """
            print the sorted list
        """
        print(sorted(self))
