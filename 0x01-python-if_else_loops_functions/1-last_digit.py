#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -1 * number
    res = number % 10
    res = -1 * res
    number = -1 * number
else:
    res = number % 10
if res > 5:
    print(f"Last digit of {number} is {res} and is greater than 5")
elif res == 0:
    print(f"Last digit of {number} is {res} and is 0")
else:
    print(f"Last digit of {number} is {res} and is less than 6 and not 0")
