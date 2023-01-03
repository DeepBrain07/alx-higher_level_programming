#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    res = number % 10
    return (res)
