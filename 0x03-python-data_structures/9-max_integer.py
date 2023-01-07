#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    list_cp = []
    for v in my_list:
        list_cp.append(v)
    for i in range(len(my_list)):
        for j in range(len(list_cp)):
            if my_list[i] < list_cp[j]:
                break
            if j == len(list_cp) - 1 and my_list[i] >= list_cp[j]:
                return (my_list[i])
