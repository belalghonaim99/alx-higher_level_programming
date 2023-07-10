#!/usr/bin/python3
"""define an inherited class check function"""


def inherits_from(obj, a_class):
    """if object is an inherited instance of a class

    Args: obj (any): The object for check
        a_class (type): class to  the type of object to
    Return:
        If object is an inherited instance of a_class return True
        Otherwise return False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
