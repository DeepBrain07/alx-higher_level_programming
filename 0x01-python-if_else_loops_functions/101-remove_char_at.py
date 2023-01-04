#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    for i in range(n):
        strcp[j] = str[i]
        j += 1
    for k in range(n, (len(str) + 1)):
        strcp[k] = str[n + 1]
    return (strcp)
