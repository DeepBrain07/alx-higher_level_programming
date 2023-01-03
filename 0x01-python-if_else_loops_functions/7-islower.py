#!/usr/bin/python3
def islower(c):
    var = ord(c)
    for i in range(97, 123):
        if i == var:
            return (True)
    return (False)
