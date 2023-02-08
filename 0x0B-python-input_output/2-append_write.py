#!/usr/bin/python3

""" This module  appends a string at the end of a text
    file (UTF8) and returns the number of characters added """


def append_write(filename="", text=""):
    """ This function appends a string at the end of a
        text and returns the number of chars added """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
