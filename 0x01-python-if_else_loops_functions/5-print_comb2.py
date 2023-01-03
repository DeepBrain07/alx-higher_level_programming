#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        var = ", "
    else:
        var = "\n"
    if i < 10:
        print("{}".format(0), end="")
    print("{}".format(i), end=var)
