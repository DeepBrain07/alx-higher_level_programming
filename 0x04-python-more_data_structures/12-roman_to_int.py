#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for rom in reversed(roman_string):
        val = digits[rom]
        if total < val * 5:
            total += val
        else:
             total -= val
    return total
