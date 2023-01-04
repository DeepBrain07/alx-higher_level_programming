#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(n, (len(str) + 1)):
        str[i] = str[n + 1]
    str[len(str)] = ""
    return (str)
