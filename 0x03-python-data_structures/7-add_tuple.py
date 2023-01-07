#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        x1 = 0
        y1 = 0
    elif len(tuple_a) == 1:
        x1 = tuple_a[0]
        y1 = 0
    elif len(tuple_a) >= 2:
        x1 = tuple_a[0]
        y1 = tuple_a[1]
    if len(tuple_b) == 0:
        x2 = 0
        y2 = 0
    elif len(tuple_b) == 1:
        x2 = tuple_b[0]
        y2 = 0
    elif len(tuple_b) >= 2:
        x2 = tuple_b[0]
        y2 = tuple_b[1]
    new_tuple = ((x1 + x2), (y1 + y2))
    return (new_tuple)
