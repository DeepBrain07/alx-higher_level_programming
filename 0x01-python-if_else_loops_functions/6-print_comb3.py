#!/usr/bin/python3
for i in range(90):
    for j in range(10):
        if j > i:
           print("{}".format(i), end="")
           print("{}".format(j), end="")
           if i != 8 and j != 9:
               var = ", "
           else:
               var = "\n"
           print(var, end="")
