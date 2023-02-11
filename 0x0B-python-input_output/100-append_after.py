#!/usr/bin/python3

""" This function defines one of the input/output functions """


def append_after(filename="", search_string="", new_string=""):
    """ This function inserts a line of text to a file,
        after each line containing a specific string """
    my_text = ""
    with open(filename) as f:
        for line in f:
            my_text += line
            if search_string in line:
                my_text += new_string
    with open(filename, "w", encoding="utf-8") as f2:
        f2.write(my_text)
