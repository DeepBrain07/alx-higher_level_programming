#!/usr/bin/python3
"""
    This module inherits from the list class
"""


class MyList(list):
    """ This class inherits from the list class """
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
