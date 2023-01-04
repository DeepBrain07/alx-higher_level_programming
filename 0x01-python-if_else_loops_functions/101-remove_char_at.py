#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(n, (len(str) + 1)):
        str[n] = str[n + 1]
        n += 1
