#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    sum = 0
    for i in range(0, (len(argv) - 1)):
        num = int(argv[i + 1])
        sum += num
    print("{:d}".format(sum))
