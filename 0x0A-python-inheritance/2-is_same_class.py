#!/usr/bin/python3
"""define class check a function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a the class

    Args: obj (any): object to check
        a_class (type): class to the type of obj
    Return:
        if obj is an instance of a_class - return True
        Otherwise return False
    """
    if type(obj) == a_class:
        return True
    return False
