#!/usr/bin/python3
"""define class and inherited class check a function"""


def is_kind_of_class(obj, a_class):
    """ if an object is an instance or inherited instance of a class

    Args: obj (any): object for check
        a_class (type): class to match type of object
    Return: If obj is an instance or inherited instance of a_class return True
        Otherwise return False
    """
    if isinstance(obj, a_class):
        return True
    return False
