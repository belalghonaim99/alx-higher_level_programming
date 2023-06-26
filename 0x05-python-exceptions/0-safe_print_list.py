#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    r = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            r += 1
        except IndexError:
            break
    print("")
    return (r)
