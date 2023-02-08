#!/usr/bin/python3

""" This module reads a text file (UTF8)
    and prints it to the STDOUT """


def read_file(filename=""):
    """ This function reads a text file """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
