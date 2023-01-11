#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return (0)
    add = 0
    add2 = 0
    for i in my_list:
        mul = 1
        for j in i:
            mul = mul * j
        add2 = add2 + i[-1]
        add = add + mul
    return (add / add2)
