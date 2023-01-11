#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_cp = []
    add = 0
    for i in range(len(my_list)):
        if my_list[i] not in list_cp:
            add += my_list[i]
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                list_cp.append(my_list[i])
    return (add)
