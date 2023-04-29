#!/usr/bin/python3
""" This module defines function finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ This function finds a peak in a list of unsorted integers """
    length = len(list_of_integers)
    if length < 1:
        peak = None
    for i in range(0, length):
        if i == 0 and list_of_integers[i] >= list_of_integers[i + 1]:
            peak = list_of_integers[i]
        elif i == length and list_of_integers[i] >= list_of_integers[i - 1]:
            peak = list_of_integers[i]
        else:
            if (i > 0) and (i < length - 1):
                if list_of_integers[i] >= list_of_integers[i - 1] or \
                   list_of_integers[i] >= list_of_integers[i + 1]:
                    peak = list_of_integers[i]
    return (peak)
