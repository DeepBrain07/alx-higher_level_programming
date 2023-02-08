#!/usr/bin/python3

""" This module writes to a text file and returns
    the number of characters written """


def write_file(filename="", text=""):
    """ Write to a text file and returns
        the number of characters written """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
