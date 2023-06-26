#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        r = 0
    for y in range(r, x):
        try:
            print("{:d}".format(my_list[y]), end="")
            r += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (r)
