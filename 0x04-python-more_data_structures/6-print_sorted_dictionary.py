#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_origin = list(a_dictionary.keys())
    list_origin.sort()
    for y in list_origin:
        print("{}: {}".format(y, a_dictionary.get(y)))
