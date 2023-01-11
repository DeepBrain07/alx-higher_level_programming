#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_cp = {}
    for d in a_dictionary:
        dict_cp[d] = a_dictionary[d]
    for i in list(dict_cp):
        dict_cp[i] *= 2
    return dict_cp
