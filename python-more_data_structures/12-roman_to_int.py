#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    length = len(roman_string)  
    for i in range(length):
        if i < length - 1 and roman_to_int_map[roman_string[i]] < roman_to_int_map[roman_string[i + 1]]:
            total -= roman_to_int_map[roman_string[i]]
        else:
            total += roman_to_int_map[roman_string[i]]
    return total
