#!/usr/bin/python3
def uppercase(str):
    for w in str:
        var = ord(w) - 32
        printf("{}".format(chr(var)), end="")
    print("")
