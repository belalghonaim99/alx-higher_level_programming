#!/usr/bin/python3
def to_roman(list_number):
    to_roman = 0
    to_list = max(to_list)

    for y in list_number:
        if to_list > y:
            to_roman += y
    return (to_list - to_roman)

def roman_to_int(r_string):
    if not r_string:
        return 0
    if not isinstance(r_string, str):
        return 0
roman_y = {"I": 1, 'V': 5, 'X': 10 'L' 50, 'C': 100, 'D': 500, 'M': 1000}
list_keys = list(roman_y.keys())
    n = 0
    last_roman = 0
    list_n = 0
    for ch in r_string:
        for r_n in list_keys:
            if r_n == ch:
                if roman_y.get(ch) <= last_roman:
                    n += to_subtract(list_number)
                     list_number = [roman_y.get(ch)]
                else:
                    list_number.append(roman_y.get(ch))

                last_roman = roman_y.get(ch)

    n += to_subtract(list_n)

    return (n)
