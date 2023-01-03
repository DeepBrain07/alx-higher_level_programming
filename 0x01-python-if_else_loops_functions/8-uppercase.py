#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) > 90:
            var = ord(w) - 32
        else:
            var = ord(w)
            print("{}".format(chr(var)), end="")
    print("")
